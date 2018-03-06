function addFavorite(){
	var url = "dh.hentaiworld.cc",title = "绅士导航";
	if(window.external && 'addFavorite' in window.external){ // IE
		window.external.addFavorite(url, title);
	} else if(window.sidebar && window.sidebar.addPanel) { // Firefox23后被弃用
		window.sidebar.addPanel(url, title);
	} else if(window.opera && window.print) { // rel=sidebar，读取a链接的href，title 注：opera也转战webkit内核了
		this.title = title;
		return true;
	} else { // webkit - safari/chrome
		spop({
			template:'按' + (navigator.userAgent.toLowerCase().indexOf('mac') !== -1 ? 'Command/Cmd' : 'CTRL') + ' + D 快速收藏本站！',
			position:'top-center',
			autoclose: 3000,
		});
	}
}

function mail(){
	spop({
		template:'<h4>反馈&建议</h4><br>发邮件至 monkeyblacktech97@gmail.com',
		style:'warning',
		position:'bottom-right',
		autoclose: 3000,
		onOpen: function () {
			document.body.style.background = "";
		},
		onClose: function() {
			document.body.style.background = "";
			spop({
			template:'感谢你的反馈&意见',
			style:'success',
			position:'bottom-right',
			autoclose: 2000,
			});
		}
	});
}

function wechat(){
	spop({
		template:'<img src="img/wechat.png"  width="240px" height="240px"/>',
		position:'top-center',
		autoclose: 3000,
	});
}

function sub_wechat(){
	spop({
		template:'<img src="../../img/wechat.png"  width="240px" height="240px"/>',
		position:'top-center',
		autoclose: 3000,
	});
}
function main(){
	spop({
		template:'你已经在首页了！',
		style:'warning',
		position:'bottom-right',
		autoclose: 3000,
	});
}