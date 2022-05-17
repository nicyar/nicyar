let form =document.getElementById('userForm')

form.addEventListener('submit',(evt)=>{
    evt.preventDefault();
    let data = new FormData(form)
    let obj = {} //queremos un json y enviarle unjson con el postman
    data.forEach((value,key)=>[key]=value); // toma el objeto que va a enviar 
    // fetch('/users',{
    //     method:'POST',
    //     body:JSON.stringify(obj),
    //     header:{
    //         "Content-Type":"application/json"//especifica que esta mandando lo lleva a user
    //     }
    // }).then(res=>res.json()).then(json=>console.log(json))
    //ahora mi formulario no va a necesitar un fetch normal 
    fetch('/users',{
        method:"POST",
        body:data
    }).then(res=>res.json()).then(json=>console.log(json))
})