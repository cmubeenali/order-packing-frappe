
frappe.pages['packing-utility'].on_page_load = function(wrapper) {	
	new PackingUtility(wrapper);
}

PackingUtility = Class.extend({
	init: function (wrapper) {
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: 'Packing Utility',
			single_column: true
		});
		this.make();		
	},
	make:function () {
		let base=$(this);
		let body=`
		<div class="row">
			<div class="col-md-4">
				<div id="current-orders">
					
				</div>
			</div>
			<div class="col-md-6">
				&nbsp;
			</div>
		</div>
		`;
		let func_fetch_orders=function(){
			$('#current-orders').empty();
			frappe.call({
				method:'order_packing.order_packing.page.packing_utility.packing_utility.fetch_all_orders',
				callback:function(data){
					for(let i=0;i<data.message.length;i++){
						let item_order=`
						<div class="card">
							<div class="card-body">
							`+data.message[i]['name']+`
							</div>
						</div>
						`
						$('#current-orders').append(item_order);
					}
				}
			})
		}
		func_fetch_orders();		
		$(frappe.render_template(body, this)).appendTo(this.page.main);		
		frappe.socketio.socket.on("new_order", (data) => { 			
			frappe.utils.play_sound('submit')
			func_fetch_orders();
		});
	}
})