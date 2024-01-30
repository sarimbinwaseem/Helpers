SUM = 0.0
ID = "ctl00_ContentPlaceHolder1_TgridAssesmentDetail_ctl00__!"

function setCharAt(str,index,chr) {
    if(index > str.length-1) return str;
    return str.substring(0,index) + chr + str.substring(index+1);
}

for (let index = 0; index < 8; index++) {
    newID = setCharAt(ID, 54, index.toString())
    ele =  document.getElementById(newID)
    eleContent = ele.children[6].textContent
    elefloat = parseFloat(eleContent)
    SUM += elefloat
}

console.log(SUM)
