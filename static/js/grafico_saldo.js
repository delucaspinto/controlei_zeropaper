var myConfig_saldo = {
  backgroundColor:'none',
 	type: "gauge",
 	plot: {
 	  arperture:180,
 	  csize:4,
 	  backgroundColor:'none',
 	  tooltip:{
 	    visible: false
 	  }
 	},
 	plotarea: {
 	  backgroundColor: 'none',
 	  borderWidth: 0,
 	  margin: "100 0 0 0"
 	},
 	scaleR: {
    minValue:0,
    maxValue:100,
    step:20,
 	  aperture:180,
	  backgroundColor:'none',
 	  item: {
 	    padding: 5,
 	    fontColor : "#1E5D9E",
 	    fontFamily: 'Montserrat',
      offsetR:0
 	  },
 	  tick: {
 	    lineColor: '#D1D3D4',
 	    placement:'out',
	    lineColor:'#1E5D9E'
 	  },
 	  center:{
 	    size:0,
 	    borderColor:'none',
 	    backgroundColor:'none'
 	  },
 	  ring:{
 	    size:3,
 	    rules:[
 	      {
 	        rule:'%v < 20',
 	        backgroundColor:'#00BAF2'
 	      },
 	      {
 	        rule:'%v >= 20 && %v < 60',
 	        backgroundColor:'#1E5D9E'
 	      },
 	      {
 	        rule:'%v >= 60 && %v < 80',
 	        backgroundColor:'#9B26AF'
 	      },
 	      {
 	        rule:'%v >= 100',
 	        backgroundColor:'#E80C60'
 	      }  
 	    ]
 	  }
 	},
	series : [
		{
		  text: "Internal",
			values : [99],
			lineColor: "#00BAF2",
			backgroundColor: "#1E5D9E",
		},
 
	]
};
 
zingchart.render({ 
	id : 'grafico_saldo', 
  	data: myConfig_saldo,
	height: 400, 
	width: '100%' 
});