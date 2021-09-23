var slideshowdiv=document.getElementById("slide");
var slideshowimagetag= document.getElementById("img");
var imgi=0;
//images for the slider
//slideshow

if(window.location.pathname == "/"){
var stringimages=slideshowimagetag.getAttribute('alt').replace(/'/g ,"")
var slicedimages=stringimages.slice(1,stringimages.length - 1 );
var images=slicedimages.split(',');


//append divs in the center element of the slider
var center= $('.center');
for(var j=0;j<images.length;j++){

    var circlediv= "<div data-num="+j +" class='circle'></div>"
    center.append(circlediv)
}



//when click on the center element of the slider ""bulls"""
var eles=document.getElementsByClassName("circle")
for(var i=0; i<eles.length;i++){
   
    
        eles[i].addEventListener("click",function(){
            //get the data-num
            var num_data=this.dataset.num;
            this.classList.add("active");
            $(this).siblings().removeClass("active");

            //on click also change the src of the image
            slideshowimagetag.setAttribute('src',images[num_data]);
            imgi=num_data
            
            
        })
        //callback function to use it when the slider is working
function circlesSlider(j){
    var eles=document.getElementsByClassName("circle")
    
        //get the data-num
    
        eles[j].classList.add("active");
        $(eles[j]).siblings().removeClass("active");
        
    
}
}
   
}




//when clicking on the gear
$(".gear-gear").on("click", function(){

    this.classList.toggle("slided");
   

    if(this.classList.contains("slided")){

        $(".gear").animate({
            'left':0
        },700);
        $("body").animate({
            'padding-left':20 + "%"
        },700);
        
        

    }else{

        $(".gear").animate({
            'left':-20 +"%"
        },500);
        $("body").animate({
            'padding-left':0
        },500);
        

    }
});






//get pathname of the current window to avoid error in the console
var voiderror=window.location.pathname== "/";



//if the current path name is "/" then 
if(voiderror){
    
   var InterVal= setInterval((e) => { 
   
        if(imgi<images.length){
            slideshowimagetag.setAttribute('src',images[imgi]);
            eles[imgi].click();
            imgi++;
           
        }
        else{
            imgi=0
           
        }
    
    }, 2000);

}
//get footer offset
var footerofsset = $("#footer").offset().top;
//get element that contain id called contact
var contactele = $("#contact");

//when click on contact animate the scollTop
contactele.on('click',function(e){
    e.preventDefault();
    $("body").animate({
        scrollTop:footerofsset    
    },1200)
})




//calltrasnlation function is the function that transalte your page
function calltranslation(url){
    var pathname=window.location.pathname;
$.ajax({
    url: "/translation/translation.json",
    data: "data",
    dataType: "json",
    success: function (data) {
      
        //get pathnames written in the json file
        var pathnames=Object.keys(Object.values(data)[0]);

        //lopp through them ' pathnames ' and check if the current path == pathname
        //to avoid errors
        pathnames.forEach((path, index1)=>{

          if(path == window.location.pathname){

            //loop through the ids and change the content
            Object.keys(data[selectedlangvalue][path]).forEach((id,index)=>{

            var content=Object.values(data[selectedlangvalue][path])[index];

           if(document.getElementById(id)){
            document.getElementById(id).textContent = content  
           }        
       })
          }
      })
      
    }
  });
}
 

////get selected language onchange
var selectedlangele= document.getElementById("select")
var selectedlangvalue=""
//
////get url path name of the json translation
var jsonfilepath="static/translation/translation.json"
//
////translate
function translate(url){
    selectedlangvalue=selectedlangele.value.toLowerCase();

    //get url path name of the json translation
    var jsonfilepath="static/translation/translation.json"
    calltranslation(url);
}
selectedlangele.addEventListener('change',function(){
    selectedlangvalue=selectedlangele.value.toLowerCase();
    calltranslation(jsonfilepath);
   localStorage.setItem("language",selectedlangvalue)
})
     //save data language on load

   //on load


window.addEventListener("load", function(){

    //get item from local storaage
   var actuallanguage=localStorage.getItem("language");
   
   //change value auto when refreshing
   selectedlangele.value=actuallanguage;

   //then translate the page
    translate(jsonfilepath)


})

//when click on images
$(".program-wrkt-thumb div img").click(function(){

    $(this).parent().addClass("active-img").siblings().removeClass("active-img");
    $(this).parent().parent().siblings(".program-wrkt-pers-info").children(".main-img").children("img").hide().attr("src", $(this).attr("src")).fadeIn(700);


});


//var thumbchildrenlength = $(".program-wrkt-thumb").children().length;
//
//var thumbchildren = $(".program-wrkt-thumb").children().length;
//var totalwidth = (thumbchildren ) * 150 ;
//var mywidth = (100 - totalwidth)/ thumbchildren ;
//var margin=mywidth/2;
//$(".program-wrkt-thumb").css({
//    "width": totalwidth +"px",
//
//});
//$(".program-wrkt-thumb div").css({
//    "margin-left": margin  + "px"
//});