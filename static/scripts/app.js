 angular.module('myApp', ['tc.chartjs','chart.js'])
 .controller("LineCtrl", function ($scope) {
  $scope.ytdrevenue = 234898846

  $scope.labels = ["2012", "2013", "2014", "2015", "2016"];
  $scope.series = ['Total Invoice'];
  $scope.data = [
  [318528419, 1230523262, 1370390439, 1648752520, 1391982311]
  ];
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };
  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }];
  $scope.options = {
    scales: {
      yAxes: [
      {  ticks: {
                    // Create scientific notation labels
                    callback: function(value, index, values) {
                      value = value.toString();
                      value = value.split(/(?=(?:...)*$)/);

            // Convert the array to a string and format the output
            value = value.join(',');
            return '₹ ' + value;
          }
        }
        ,
        id: 'y-axis-1',
        type: 'linear',
        display: true,
        position: 'left'
      }
      ]
    }


  };
})
.controller("zoneCtrl", function ($scope) {
  $scope.ytdrevenue = 234898845.96

  $scope.labels = ['Jan-2013' ,'Feb-2013',  'Mar-2013',  'Apr-2013' , 'May-2013'  ,'Jun-2013' , 'Jul-2013' , 'Aug-2013'  ,'Sep-2013' , 'Oct-2013' , 'Nov-2013' , 'Dec-2013' , 'Jan-2014'  ,'Feb-2014' , 'Mar-2014' , 'Apr-2014' , 'May-2014' , 'Jun-2014' , 'Jul-2014' , 'Aug-2014' , 'Sep-2014'  ,'Oct-2014' , 'Nov-2014' , 'Dec-2014' , 'Jan-2015',  'Feb-2015', 'Mar-2015' , 'Apr-2015' , 'May-2015' , 'Jun-2015' , 'Jul-2015' , 'Aug-2015' , 'Sep-2015' , 'Oct-2015' , 'Nov-2015'  ,'Dec-2015'  ,'Jan-2016' , 'Feb-2016' , 'Mar-2016',  'Apr-2016' , 'May-2016' , 'Jun-2016' , 'Jul-2016' , 'Aug-2016' , 'Sep-2016'  ,'Oct-2016' , 'Nov-2016' , 'Dec-2016',  'Jan-2017',  'Feb-2017','Mar-2017','Apr-2017'];
  $scope.series = ['Actual', 'Predicted'];
  $scope.data = [
  [36267,36207,41421,16233,18587,19995,20698,22144,22379,20917,20285,22441,18601,21584,22877,16323,19575,26874,29825,25398,29694,25978,32295,31191,28297,33497,34650,30554,30841,35513,36737,35974,35216,32776,35411,37703,27839,34474,34509,29493,25222,22918,16250,16229,13552,19489,15940,17056,1170,11882],
  [36267, 33194.702980166665, 38537.74769717964, 13130.965756316868, 15426.64086875472, 16852.569027344776, 17577.014057445194, 19291.86320511614, 19629.57453561742, 18161.672489384608, 17505.73595927781, 19819.90238889579, 16039.400895026292, 19094.469098059853, 20436.76367816892, 13866.547859160952, 17229.98133037913, 24696.89350284371, 27773.858089351823, 23414.84872754783, 27819.049345464755, 24075.429432710498, 30475.87460253967, 29500.976859918163, 26617.892134857153, 31917.188609000954, 33099.85079670368, 29030.79837884546, 29371.80463352741, 34122.73495518508, 35391.40110543631, 34709.263690157175, 34004.13846896458, 31517.792774423535, 34162.35547329891, 36556.359653043466, 26631.934408307443, 33328.075059198745, 33375.52416267451, 28307.435294365423, 24044.705416627763, 21660.714444360354, 14845.772261894766, 14798.709410836953, 12158.946803494364, 18193.938677401005, 14662.0317860303, 15792.249230996003, -265.5614805524169, 10478.708484571289, 6600.770626462612, 7029.660772441059]
  ]
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };
  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }];
  $scope.options = {
    scales: {
      yAxes: [
      {  ticks: {
                    // Create scientific notation labels
                    callback: function(value, index, values) {
                      value = value.toString();
                      value = value.split(/(?=(?:...)*$)/);

            // Convert the array to a string and format the output
            value = value.join(',');
            return value + " Ml";
          }
        }
        ,
        id: 'y-axis-1',
        type: 'linear',
        display: true,
        position: 'left'
      }
      ]
    }


  };
})

.controller("cust_produCtrl", function ($scope) {
  $scope.ytdrevenue = 234898845.96

  $scope.labels = ['Jan-2013' ,'Feb-2013',  'Mar-2013',  'Apr-2013' , 'May-2013'  ,'Jun-2013' , 'Jul-2013' , 'Aug-2013'  ,'Sep-2013' , 'Oct-2013' , 'Nov-2013' , 'Dec-2013' , 'Jan-2014'  ,'Feb-2014' , 'Mar-2014' , 'Apr-2014' , 'May-2014' , 'Jun-2014' , 'Jul-2014' , 'Aug-2014' , 'Sep-2014'  ,'Oct-2014' , 'Nov-2014' , 'Dec-2014' , 'Jan-2015',  'Feb-2015', 'Mar-2015' , 'Apr-2015' , 'May-2015' , 'Jun-2015' , 'Jul-2015' , 'Aug-2015' , 'Sep-2015' , 'Oct-2015' , 'Nov-2015'  ,'Dec-2015'  ,'Jan-2016' , 'Feb-2016' , 'Mar-2016',  'Apr-2016' , 'May-2016' , 'Jun-2016' , 'Jul-2016' , 'Aug-2016' , 'Sep-2016'  ,'Oct-2016' , 'Nov-2016' , 'Dec-2016',  'Jan-2017',  'Feb-2017','Mar-2017','Apr-2017'];
  $scope.series = ['Actual', 'Predicted'];
  $scope.data = [
  [2182,2575,1505,2438,2248,2242,2299,2016,2280,2076,2435,1949,1776,2524,2198,2192,1681,948,900,1030,947,914,869,997,1004,797,668,371,411,1171,747,395,346,310,415,273,343,269,277,293,271,291,231,386,262,296,250,168,22,235],
  [2182, 2586.103601833333, 1504.280173527516, 2444.7602347048532, 2255.6283606975167, 2246.3764540875936, 2311.037644023316, 2019.9866069706663, 2285.0828455579967, 2077.7505291386356, 2444.3173845608085, 1954.0010264673845, 1772.847718216336, 2529.0722452925806, 2203.0250204664526, 2199.8359462619223, 1680.9926991555033, 926.6508426274677, 871.1142366959031, 1003.3763752583395, 923.8614396084088, 891.2037172559894, 843.682690580056, 972.0483978559718, 982.6695113023991, 774.8314106933392, 642.1952219494988, 337.36507683430693, 376.11118437159007, 1150.1075352756366, 727.3342998061403, 369.2334261533384, 315.49690568852344, 273.9431521154913, 383.69122558683796, 244.5535548161261, 315.1569572367839, 237.66101968187579, 245.61258824403, 265.49059327410794, 244.35714384650814, 263.6831905730359, 202.5526775859526, 361.3921242026622, 238.16601911798742, 271.9320089268259, 225.33658488979435, 141.8597247068065, -5.182463753999883, 209.98766164839392, 152.48258352889, 126.76496751727223] 
  ];
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };
  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }];
  $scope.options = {
    scales: {
      yAxes: [
      {  ticks: {
                    // Create scientific notation labels
                    callback: function(value, index, values) {
                      value = value.toString();
                      value = value.split(/(?=(?:...)*$)/);

            // Convert the array to a string and format the output
            value = value.join(',');
            return value + " Ml";
          }
        }
        ,
        id: 'y-axis-1',
        type: 'linear',
        display: true,
        position: 'left'
      }
      ]
    }


  };
})

.controller("branch_produCtrl", function ($scope) {
  $scope.ytdrevenue = 234898845.96

  $scope.labels = ['Jan-2013' ,'Feb-2013',  'Mar-2013',  'Apr-2013' , 'May-2013'  ,'Jun-2013' , 'Jul-2013' , 'Aug-2013'  ,'Sep-2013' , 'Oct-2013' , 'Nov-2013' , 'Dec-2013' , 'Jan-2014'  ,'Feb-2014' , 'Mar-2014' , 'Apr-2014' , 'May-2014' , 'Jun-2014' , 'Jul-2014' , 'Aug-2014' , 'Sep-2014'  ,'Oct-2014' , 'Nov-2014' , 'Dec-2014' , 'Jan-2015',  'Feb-2015', 'Mar-2015' , 'Apr-2015' , 'May-2015' , 'Jun-2015' , 'Jul-2015' , 'Aug-2015' , 'Sep-2015' , 'Oct-2015' , 'Nov-2015'  ,'Dec-2015'  ,'Jan-2016' , 'Feb-2016' , 'Mar-2016',  'Apr-2016' , 'May-2016' , 'Jun-2016' , 'Jul-2016' , 'Aug-2016' , 'Sep-2016'  ,'Oct-2016' , 'Nov-2016' , 'Dec-2016',  'Jan-2017',  'Feb-2017','Mar-2017','Apr-2017'];
  $scope.series = ['Actual', 'Predicted'];
  $scope.data = [
  [12298,14119,13960,12193,12351,13489,14294,12694,13115,13061,14532,16912,14125,16375,17163,14159,13172,11885,13287,14867,12466,18990,16356,18302,16068,15973,16618,18685,16741,81741,24684,34329,50857,20465,19876,13992,19079,21037,22866,25180,18243,19114,13304,18527,16251,15844,16394,12124,1566,4214],
  [12298, 14113.125807166667, 14013.827426366108, 12243.795833660757, 12391.895681289385, 13490.966483212556, 14328.813966523769, 12744.856592581802, 13170.339103041573, 13076.361105681763, 14559.100378599083, 17015.773829129474, 14222.014905471946, 16470.271426034178, 17259.372764106873, 14218.42009662822, 13226.479452198968, 11888.442484255798, 13272.9813999038, 14896.600458508985, 12500.788414378276, 19110.308574961113, 16456.140476794826, 18414.095760874454, 16189.8235718909, 16049.899559152711, 16697.686790409694, 18784.22352251049, 16858.668209441865, 82826.66634466933, 25424.492009018366, 34897.12084133553, 51662.613658974136, 20550.344438406057, 20087.018281878685, 14071.137292056668, 19048.25691614726, 20992.93341642327, 23022.470341561242, 25463.432400097794, 18343.469128855784, 19085.102702784236, 13230.409293748227, 18541.981046053625, 16269.804487556019, 15779.31973610486, 16363.681375567985, 12034.051560826008, 1305.9507927952327, 3866.0529129580495, 3998.68614722481, 2183.412465122091] 
  ];
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };
  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }];
  $scope.options = {
    scales: {
      yAxes: [
      {  ticks: {
                    // Create scientific notation labels
                    callback: function(value, index, values) {
                      value = value.toString();
                      value = value.split(/(?=(?:...)*$)/);

            // Convert the array to a string and format the output
            value = value.join(',');
            return value + " Ml" ;
          }
        }
        ,
        id: 'y-axis-1',
        type: 'linear',
        display: true,
        position: 'left'
      }
      ]
    }


  };
})

  .controller("Line_milkCtrl", function ($scope) {
  

  $scope.labels = ['Jan-16','Feb-16','Mar-16','Apr-16','May-16','Jun-16','Jul-16','Aug-16','Sep-16','Oct-16','Nov-16','Dec-16','Jan-17','Feb-17','Mar-17','Apr-17','May-17'];
  $scope.series = ['Actual WPI', 'Predicted WPI'];
  $scope.colours = ['#72C02C', '#3498DB'];
  $scope.data = [
  [250.8,251.7,253.9,254.6,255.6,258,259.7,260.6,261.7,261.6,261.3,261.2,261.3,261.6,262],
  [250.8, 253.13014341666664, 255.32299760667132, 256.00055638638753, 257.0246199518455, 259.4391923703322, 261.1325532761245, 262.0176594557119, 263.12863806062927, 263.004061963007, 262.65403361253834, 262.5064766191505, 262.5791692695903, 262.85950131066653, 263.2353437663889, 263.9287601123407, 264.7815867600776]
  ];
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };
  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }];
  $scope.options = {
    scales: {
      yAxes: [
      {  ticks: {
                    // Create scientific notation labels
                    callback: function(value, index, values) {
                      value = value.toString();
                      value = value.split(/(?=(?:...)*$)/);

            // Convert the array to a string and format the output
            value = value.join(',');
            return  value;
          }
        }
        ,
        id: 'y-axis-1',
        type: 'linear',
        display: true,
        position: 'left'
      }
      ]
    }


  };
})

.controller("Line_sugarCtrl", function ($scope) {
  

  $scope.labels = ['Jan-16','Feb-16','Mar-16','Apr-16','May-16','Jun-16','Jul-16','Aug-16','Sep-16','Oct-16','Nov-16','Dec-16','Jan-17','Feb-17','Mar-17','Apr-17','May-17'];
  $scope.series = ['Actual WPI', 'Predicted WPI'];
  $scope.colours = ['#72C02C', '#3498DB'];
  $scope.data = [
  [180.5,187.1,190.3,203,206.4,208.3,213,215.5,215.9,219.2,221.5,219.3,221.7,226.8,227],
  [180.5, 192.29316685, 195.43891618779162, 208.15271726805818, 211.71711007493732, 213.57605015382634, 218.219824650587, 220.5547098970917, 220.92178179502312, 224.20175037988398, 226.43162353255207, 224.0300614654914, 226.356251158167, 231.45482595401998, 231.59011213909295, 233.84512173299433, 237.73250750741042]

  ];
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };
  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }];
  $scope.options = {
    scales: {
      yAxes: [
      {  ticks: {
                    // Create scientific notation labels
                    callback: function(value, index, values) {
                      value = value.toString();
                      value = value.split(/(?=(?:...)*$)/);

            // Convert the array to a string and format the output
            value = value.join(',');
            return  value;
          }
        }
        ,
        id: 'y-axis-1',
        type: 'linear',
        display: true,
        position: 'left'
      }
      ]
    }


  };
})
    .controller("Liffe_Ctrl", function ($scope) {
  

  $scope.labels = ['07/04/17','10/04/17','11/04/17','12/04/17','13/04/17','17/04/17','18/04/17','19/04/17','20/04/17','21/04/17','24/04/17','25/04/17','26/04/17','27/04/17','28/04/17','01/05/17','02/05/17','03/05/17','04/05/17','05/05/17','08/05/17','09/05/17','10/05/17','11/05/17','12/05/17','15/05/17','16/05/17','17/05/17','18/05/17'];
  $scope.series = ['Actual WPI', 'Predicted WPI'];
  $scope.colours = ['#72C02C', '#3498DB'];
  $scope.data = [
  [2197,2183,2201,2188,2175,2175,2192,2179,2136,2012,1963,1940,1955,1938,1971,1971,2017,2061,2022,2030,2059,2053,2045,2014,2023,1998,1989],
  [2197, 2179.826108333333, 2198.1211576674, 2185.3316362511114, 2171.711286343933, 2171.7619005395286, 2189.041598301861, 2176.2771629724916, 2132.5289441068576, 2006.3154033201727, 1955.3470894826362, 1931.490940881927, 1946.6553256593045, 1930.217767823843, 1963.7914436216488, 1964.0488631477865, 2010.756165739051, 2056.3468388785245, 2017.326470126216, 2025.3589551430946, 2054.5305815880697, 2048.7425211321624, 2041.136015817288, 2009.7842728934797, 2018.339349636708, 1992.9604743944583, 1984.005589530613, 1971.2881185077972, 1994.664242744473]

  ];
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };
  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }];
  $scope.options = {
    scales: {
      yAxes: [
      {  ticks: {
                    // Create scientific notation labels
                    callback: function(value, index, values) {
                      value = value.toString();
                      value = value.split(/(?=(?:...)*$)/);

            // Convert the array to a string and format the output
            value = value.join(',');
            return  '$ ' + value;
          }
        }
        ,
        id: 'y-axis-1',
        type: 'linear',
        display: true,
        position: 'left'
      }
      ]
    }


  };
})
 .controller("DoughnutCtrl", function ($scope) {
  $scope.labels = ["Andhra", "East", "Karnataka","Kerala", "North", "South Asia", "Tamil Nadu", "West"];
  $scope.data = [20018230.54, 12024531.7, 34622404.85, 6430965.74, 43904757.34, 3262306.78, 67623993.73, 43639231.2];
  $scope.options = {legend: {display: true}};
})
 .controller("BarCtrl", function ($scope) {
  $scope.labels = ['Chennai', 'Bangalore', 'Mumbai', 'New Delhi', 'Secunderabad', 'Gurgaon', 'Pune','Kolkata','Cochin','Coimbatore','Jaipur','Noida','Vellore','Goa','ROTN','Ahmedabad','Sri lanka','Vijayawada','Nepal','Maldives','Bhutan','Tirupathi'];
  $scope.series = ['Invoice YTD'];

  $scope.data = [
    [57321803.58, 34622404.85, 26788320.39, 19995996.21, 18591194.89, 14679655.73, 12459479.45, 12024531.7,6430965.74,6265897.82,4894191.71,4334913.69,2706280.43,2523925.7,1867505.66,1674041.63,1362195.65,1330011.9,1198712,316153.15,73400,64840]
  ]
  $scope.options = {
    scales: {
      yAxes: [
      {  ticks: {
                    // Create scientific notation labels
                    callback: function(value, index, values) {
                      value = value.toString();
                      value = value.split(/(?=(?:...)*$)/);

            // Convert the array to a string and format the output
            value = value.join(',');
            return '₹ ' + value;
          }
        }
        ,
        id: 'y-axis-1',
        type: 'linear',
        display: true,
        position: 'left'
      }
      ]
    }


  };
})
 .controller("BarCustCtrl", function ($scope) {
  $scope.labels = ['Cognizant (Chennai)', 'Standard Chartered Global', 'Coffee Hut', 'The Host Services', 'Cognizant (Pune)', 'Amazon (Chennai)', 'Amazon (Goa)','Sleek International','CMC Vellore','Kumar Beverages'];
  $scope.series = ['Invoice YTD'];

  $scope.data = [
    [9235036.05, 4009374, 3701453.53, 2679920, 2612290, 2396839.25, 2353547.1, 2325349.6,2250292,2223857.75]
  ]
  $scope.options = {
    scales: {
      yAxes: [
      {  ticks: {
                    // Create scientific notation labels
                    callback: function(value, index, values) {
                      value = value.toString();
                      value = value.split(/(?=(?:...)*$)/);

            // Convert the array to a string and format the output
            value = value.join(',');
            return '₹ ' + value;
          }
        }
        ,
        id: 'y-axis-1',
        type: 'linear',
        display: true,
        position: 'left'
      }
      ]
    }


  };
})
 .filter('INR', function () {        
  return function (input) {
    if (! isNaN(input)) {
      var currencySymbol = '₹';
            //var output = Number(input).toLocaleString('en-IN');   <-- This method is not working fine in all browsers!           
            var result = input.toString().split('.');

            var lastThree = result[0].substring(result[0].length - 3);
            var otherNumbers = result[0].substring(0, result[0].length - 3);
            if (otherNumbers != '')
              lastThree = ',' + lastThree;
            var output = otherNumbers.replace(/\B(?=(\d{2})+(?!\d))/g, ",") + lastThree;
            
            if (result.length > 1) {
              output += "." + result[1];
            }            

            return currencySymbol + output;
          }
        }
      }).config(['ChartJsProvider', function (ChartJsProvider) {
    // Configure all charts
    ChartJsProvider.setOptions({
      responsive: true,
      pointDotRadius: 1,
      fill: false
    });
    
  }])

 .config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('//').endSymbol('//');
});