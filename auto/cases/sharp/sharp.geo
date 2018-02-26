cl__1 = 0.005;
Point(1000) = {0, 0, 0, 0.005};
Point(1001) = {0, 1, 0, 0.005};
Point(1002) = {5, 1, 0, 0.005};
Point(1003) = {5, 0, 0, 0.005};
Point(1004) = {1.2, 1, 0, 0.005};
Point(1005) = {3.8, 1, 0, 0.005};
Point(1006) = {1.8, 1.8, 0, 0.005};
Point(1007) = {3.2, 1.8, 0, 0.005};

top = 14.0;
left = -10.0;
right = 25.0;
bottom = -0.3;

Point(1008) = {left, top, 0, 1.0};
Point(1009) = {left, bottom, 0, 1.0};
Point(1010) = {right, top, 0, 1.0};
Point(1011) = {right, bottom, 0, 1.0};

Line(1) = {1000, 1001};
Line(2) = {1001, 1004};
Line(3) = {1004, 1006};
Line(4) = {1006, 1007};
Line(5) = {1007, 1005};
Line(6) = {1005, 1002};
Line(7) = {1002, 1003};
Line(8) = {1003, 1000};

Line(9) = {1009, 1008};
Line(10) = {1008, 1010};
Line(11) = {1010, 1011};
Line(12) = {1011, 1009};

Line Loop(1) = {1,2,3,4,5,6,7,8};
Line Loop(2) = {9,10,11,12};

Plane Surface(3) = {1, 2};

Extrude {0,0,0.8} {
	Surface{3};
	Layers{1};
	Recombine;
}

Physical Surface("frontback") = {3, 74};
Physical Surface("topbottom") = {61, 69};
Physical Surface("inlet") = {73};
Physical Surface("outlet") = {65};
Physical Surface("car") = {29, 33, 37, 41, 45, 49, 53, 57};
Physical Volume("internal") = {1};



