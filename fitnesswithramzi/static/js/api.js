//function api(){
//    url="/apimages/"
//    fetch(url,{
//        method:"POST",
//        headers:{
//            "content-type":"application/json",
//            "X-CSRFToken":csrftoken
//        },
//        body: JSON.stringify({
//            "productId":"ss",
//            "action":"sssss"
//            
//        })
//    })
//    .then((response)=>{
//        return response.json()
//    })
//    .then((data)=>{
//        //
//        console.log(data)
//    
//       
//        //
//    })
//}
//window.addEventListener("load", function(){
//    api();
//    
//})
if( window.location.pathname == "/coaching/"){
    //on click on the chekbox
checkboxelem = document.getElementById("check0")
checkboxelef = document.getElementById("check1")

checkboxelem.addEventListener("change",function(){
        if((checkboxelef.checked) && (checkboxelem.checked)){
            this.ckecked = true
            checkboxelef.checked = false
        }
    })

checkboxelef.addEventListener("change",function(){
        if((checkboxelef.checked) && (checkboxelem.checked)){
            this.ckecked = true
            checkboxelem.checked = false
        }
    })
}

if((window.location.pathname== "/program/nutrition/") || (window.location.pathname== "/program/exercises/") || (window.location.pathname== "/program/")){
    selectex=document.getElementById("slctex")
    selectex.addEventListener("change",(e)=>{
       selectedvalue = selectex.options[selectex.selectedIndex].value

     
   url="/api/"
   fetch(url,{
       method:"POST",
       headers:{
           "content-type":"application/json",
           "X-CSRFToken":csrftoken
       }
   })
   .then((response)=>{
       return response.json()
   })
   .then((data)=>{
       //
       console.log(data)
   
      
       //
   })
    })
}