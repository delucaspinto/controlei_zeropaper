var myChart = {
  "type": "line",
  "title": {
    "text": "Grafico de gastos por dia"
  },
  "plot": {
    "value-box": {
      "text": "R$ %v",
      "font-size": "12"
    },
    "tooltip": {
      "text": "R$ %v",
      "font-size": "40"
    }
  },
  "scale-x": {
    "values": lista_datas
  },
  "series": [
    {
      "values": lista_valores,
      "palette": 0
    },
  ]
};
zingchart.render({
  id: "myChart",
  data: myChart,
  height: "480",
  width: "100%"
});