function count(type){
    const resultElement = document.getElementById('result');
    const monthElement = document.getElementById('month');
    let number = resultElement.innerText;

    if(type === 'plus'){
        number = parseInt(number) + 1;
    }
    else if(type === 'minus') {
        number = parseInt(number) - 1;
    }

    resultElement.innerText = number;
    monthElement.innerText = number;
}

function input(){
    const dday = document.querySelector("#input_date").value;
    const date_before = dday.split('-');

    const yearP = date_before[0];
    const monthP = date_before[1];
    const dayP = date_before[2];

    const monthPElement = document.getElementById('result_month');
    monthPElement.innerText = parseInt(monthP) + 1;

    const dayPElement = document.getElementById('result_day');
    dayPElement.innerText = dayP;

    console.log(dayP);
}