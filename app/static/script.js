



$(document).ready(function() 
{
    var url = "https://api.thingspeak.com/channels/1679864/fields/1.json?api_key=0GUI4SCAWE6Y1S03"
    $.getJSON(url,function(data)
    {
        console.log(data)
        // console.log(data.feeds.length)
        // console.log(data.feeds[data.feeds.length-1])
        var curr = []
        curr.push(data.feeds[data.feeds.length-1])
        console.log(curr)
        console.log(curr[0].field1)
        console.log(data.feeds[0].entry_id)


        $("#active").append(curr[0].field1)

        const labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
          ];
        
          const data1 = {
            labels: curr.entryid,
            datasets: [{
              label: 'My First dataset',
              backgroundColor: 'rgb(255, 99, 132)',
              borderColor: 'rgb(255, 99, 132)',
              data: curr.field1,
            }]
          };
        
          const config = {
            type: 'line',
            data: data1,
            options: {}
          };
        
          const myChart = new Chart(
            document.getElementById('myChart'),
            config
          );

    }
    )
}
)



  