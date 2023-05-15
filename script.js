function CalcQuadrado(){
    let numeros = document.getElementById("numeros").value;
    numeros = numeros.split(",")
    for(i=0;i<numeros.length;i++){
        quadrado=numeros[i]*numeros[i];
        quadrado= parseInt(numeros[i])*parseInt(numeros[i]);
        document.write("o quadrado de "+numeros[i] +" é "+quadrado+"<br>");
    }
}