window.onload = function() {
  var ctx = document.getElementById('myChart').getContext('2d');

  const chartData = {
      chart1: {
          type: 'line',
          labels: ['China', 'India', 'Russia', 'United States', 'France'],
          data: [138.4, 112.5, 92.5, 45.3, 37.5],
          label: 'Wheat Production [MMT]'
      },
      chart2: {
          type: 'bar',
          labels: ['India', 'United States', 'China', 'Brazil', 'Australia'],
          data: [1.8, 4.06, 5.14, 2.66, 3.69],
          label: 'Agricultural Land (million sq. km)'
      },
      chart3: {
          type: 'polarArea',
          labels: ['Services Sector', 'Industrial Sector', 'Agriculture Sector', 'Construction Sector'],
          data: [53, 25, 18, 7],
          label: 'GDP Share in %'
      },
      chart4: {
          type: 'line',
          labels: ['China', 'India', 'Indonesia', 'Bangladesh'],
          data: [145.3, 145.0, 54.7, 39.1],
          label: 'Rice Production [MMT] 2023'
      },
      chart5: {
          type: 'line',
          labels: ['Brazil', 'India', 'Thailand', 'China'],
          data: [45.54, 34.3, 14.87, 11.76],
          label: 'Sugar Production [MMT] 2023'
      },
      chart6: {
        type: 'pie',
        labels: ['Wheat','Rice','Sugar','Maize','Other Crops'],
        data: [112.5,145.0,34.3,34.0,220.0],
        label: 'India Top Production [MMT] 2023'
    }
  };

  let myChart;

  window.showChart = function(chartId) {
      document.getElementById("chartContainer").style.display = "block";

      if (myChart) {
          myChart.destroy();
      }

      myChart = new Chart(ctx, {
          type: chartData[chartId].type,
          data: {
              labels: chartData[chartId].labels,
              datasets: [{
                  label: chartData[chartId].label,
                  data: chartData[chartId].data,
                  backgroundColor: [
                      'rgba(255, 99, 132, 1)',
                      'rgba(54, 162, 235, 1)',
                      'rgba(255, 206, 86, 1)',
                      'rgba(75, 192, 192, 1)',
                      'rgba(153, 102, 255, 1)'
                  ]
              }]
          },
          options: {
              responsive: true,
              maintainAspectRatio: false,
              scales: {
                  y: {
                      beginAtZero: true
                  }
              }
          }
      });
  };

  window.closeChart = function() {
      document.getElementById("chartContainer").style.display = "none";
      if (myChart) {
          myChart.destroy();
      }
  };
};
