



$(document).ready(function() 
{
    var url = "https://api.thingspeak.com/channels/1679864/fields/1.json?api_key=0GUI4SCAWE6Y1S03"
    $.getJSON(url,function(data)
    {
        console.log(data)
        // console.log(data.feeds.length)
        // console.log(data.feeds[data.feeds.length-1])
        var curr = []
        var moisture = []
        var entry_id = []
        curr.push(data.feeds[data.feeds.length-1])
        console.log(curr)
        console.log(curr[0].field1)
        console.log(data.feeds[0].entry_id)
        $.each(data.feeds,function(id,obj)
        {
          moisture.push(obj.field1)
          entry_id.push(obj.entry_id)
          
          
        })
        console.log(moisture)
        var moisture_val = []
        var entry_id_val = []

        for (let i =  moisture.length - 1; i > moisture.length - 10; i--) {
            
              moisture_val.push(moisture[i]);
              entry_id_val.push(entry_id[i])

            
          }
          console.log(moisture_val)


        $("#active").append(curr[0].field1)

        
        var chart = document.getElementById("myChart").getContext("2d");
          var chart = new Chart(myChart,{
            type : "bar",

            data : {
            labels : entry_id_val,
              
              datasets : [
                {
                  label : "Daily Confirmed Cases",
                  data : moisture_val,
                  backgroundColor : "#cf2b5f",
                  borderColor:"#cf2b5f",
                  minBarLength : 100,
                  borderWidth : 3,
                  pointRadius:1,
                  
                  fill : false
                }
              ]
            },
            options : {
              responsive : false,
              legend: {
                labels: {
                    fontColor: '#cf2b5f',
                    fontFamily:"'Montserrat', sans-serif"

                    
                    // fontSize: 18
                }
            },
              scales: {
                xAxes: [{
                    gridLines: {
                        display:false,
                        color: '#cf2b5f'

                    },
                    ticks:{
                      maxTicksLimit:8,
                      fontColor : '#A4A8CD',
                      fontSize: 9,
                      fontFamily:"'Montserrat', sans-serif"

                    }
                }],
                yAxes: [{
                    gridLines: {
                        display:false,
                        color: '#cf2b5f'
                    },
                    ticks:{
                      maxTicksLimit:8,
                      fontColor : '#A4A8CD',
                      fontSize: 9,
                      fontFamily:"'Montserrat', sans-serif"
                    }   
                }]
            }
              // scales:{
              //   x:{
                  
                
              //     // min : '22 November',
              //     // max : '22 November'
              //   }
              // }

            }
          })
         

    }
    )
}
)



  
// const button = document.querySelector("button");

    if(navigator.geolocation){
        // button.innerText = "Allow to detect location";
        navigator.geolocation.getCurrentPosition(onSuccess, onError);
    }

function onSuccess(position){
    // button.innerText = "Detecting your location...";
    let {latitude, longitude} = position.coords;
    fetch(`https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=0d5653a2749e4feb80741437ccfd1689`)
    .then(response => response.json()).then(response =>{
        let allDetails = response.results[0].components;
        console.table(allDetails);
        let {suburb, town, state} = allDetails;
        
        // button.innerText = `${county} ${postcode}, ${country}`;
        document.getElementById("location").innerHTML =`${suburb} ${town}, ${state}`;

    }).catch(()=>{
        // button.innerText = "Something went wrong";
        document.getElementById("location").innerHTML ="Something went wrong";


    });
}
function onError(error){
    if(error.code == 1){
        button.innerText = "You denied the request";
    }else if(error.code == 2){
        button.innerText = "Location is unavailable";
    }else{
        button.innerText = "Something went wrong";
    }
    button.setAttribute("disabled", "true");
}
