var age = document.getElementById("age");
var height = document.getElementById("height");
var weight = document.getElementById("weight");
var form = document.getElementById("form");
let resultArea = document.querySelector(".comment");

modalContent = document.querySelector(".modal-content");
modalText = document.querySelector("#modal-text");
var modal = document.getElementById("my_modal");
var span = document.getElementsByClassName("close")[0];


function calculate(){
    if(age.value=='' || height.value=='' || weight.value=='') {
        modal.style.display = "none";
        modalText.innerHTML = `All fields are required!`;
    }else{
        countBmi();
    }
}

function countBmi(){
    var p = [age.value, height.value, weight.value];

    var bmi = Number(p[2])/(Number(p[1])/100*Number(p[1])/100);
      
    var result = '';
    if(bmi<16){
        result = 'Severely Underweight';
    }else if(16<=bmi&&bmi<=16.9){
        result = 'Moderately Underweight';
    }else if(17<=bmi&&bmi<=18.4){
        result = 'Mildly Underweight';
    }else if(18.5<=bmi&&bmi<=24.9){
        result = 'Normal Weight';
    }else if(25<=bmi&&bmi<=29.9){
        result = 'Overweight';
    }else if(30<=bmi&&bmi<=34.9){
        result = 'Obese Type I';
    }else if(35<=bmi&&bmi<=39.9){
        result = 'Obese Type II';
    }else if(40<=bmi){
        result = 'Obese Type III';
    }

resultArea.style.display = "block";
document.querySelector(".comment").innerHTML = `You are <span id="comment">${result}</span>`;
document.querySelector("#result").innerHTML = bmi.toFixed(2);
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
