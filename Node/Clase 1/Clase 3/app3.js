console.log('Inicio del programa');
setTimeout(()=> {
console.log('Primer timeout');//5
}, 3000);

setTimeout(()=> {
    console.log('Segundo timeout');//2
    }, 0);

    setTimeout(()=> {
        console.log('Tercero timeout'); //3
        }, 0);

        console.log('Fin del programa'); //4