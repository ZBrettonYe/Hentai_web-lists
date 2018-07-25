from django.contrib import admin
from .models import Site, Category, SmallCategory

admin.site.site_header = '管理系统'


class SiteInline(admin.TabularInline):
    model = Site
    extra = 6

class SiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'smallcategory', 'category', 'image_url', 'true_url', 'created_time']
    search_fields = ('name',)
    date_hierarchy = 'created_time'
    ordering = ['id']

    # 显示是否国内
    def category(self, obj):
        return '%s' % obj.smallcategory.category.name

    category.short_description = '大分类'


class SmallCategoryInline(admin.TabularInline):
    model = SmallCategory


class SmallCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'guonei', 'created_time']
    list_filter = ('category',)
    search_fields = ('name',)
    date_hierarchy = 'created_time'
    ordering = ['id']
    inlines = [SiteInline]

    # 显示是否国内
    def guonei(self, obj):
        return '%s' % ('国内' if obj.category.guonei else '国外')

    guonei.short_description = '国内'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'guonei', 'created_time']
    search_fields = ('name',)
    date_hierarchy = 'created_time'
    ordering = ['id']
    inlines = [SmallCategoryInline]


admin.site.register(Site, SiteAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SmallCategory, SmallCategoryAdmin)
