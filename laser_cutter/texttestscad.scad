
difference() {
scale([1,1,-1]){
	import("PoopButton.stl");
}
	translate([-16, -5, 5]) {
scale([.6, .6, .6]){
		linear_extrude(height = 100, center = true, convexity = 10)
		import("testtext.dxf");
}
	}
}



