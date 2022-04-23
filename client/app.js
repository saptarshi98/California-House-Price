function getLong() {
  var ln = document.getElementById("uiLong").value;
  console.log(ln);
    return parseFloat(ln);
}
function getLat() {
    var lt = document.getElementById("uiLat").value;
      return parseFloat(lt);
  
  }
  function getAge() {
    var a = document.getElementById("uiAge").value;
      return parseInt(a);
  
  }
  function getRoom() {
    var r = document.getElementById("uiRoom").value;
      return parseInt(r);
  
  }
  function getBedroom() {
    var b = document.getElementById("uiBedroom").value;
      return parseInt(b);
  
  }
  function getHousehold() {
    var h = document.getElementById("uiHousehold").value;
      return parseInt(h);
  
  }
  function getPopulation() {
    var p = document.getElementById("uiPopulation").value;
      return parseInt(p);
  
  }
  function getIncome() {
    var i = document.getElementById("uiIncome").value;
      return parseFloat(i);
  
  }

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var long = getLong()
  var lat = getLat();
  var age = getAge();
  var room = getRoom();
  var bedroom = getBedroom();
  var population = getPopulation();
  var household = getHousehold();
  var income = getIncome();
  var estPrice = document.getElementById("uiEstimatedPrice");
  var location = document.getElementById("uiLocations").value;
  console.log(location);


  var url = "http://127.0.0.1:5000/predict_price"; 
  console.log("est = " + estPrice);

  $.post(url, {
      long: long,
      lat: lat,
      age: age,
      room: room,
      bedroom: bedroom,
      population: population,
      household: household,
      income: income,
      proximity : location
      
  },function(data, status) {
    console.log(data.estimated_price);
    estPrice.innerHTML = "<h2>$ " + data.estimated_price.toString() + " </h2>";
    console.log(estPrice)
    console.log(status);
  });
}