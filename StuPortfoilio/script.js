var timeout;
function HPA(){
    var tl = gsap.timeline();

    tl.from("#nav",{
        y:"-10",
        opacity:0,
        duration:1.2,
        ease:Expo.easeInOut
    })
    .to(".h",{
       y:0,
       duration:2,
       ease:Expo.easeInOut,
       stagger:.2,
       delay:-.7
    })
    .from("#footer",{
        y:'-30',
        opacity:0,
        duration:1.2,
        ease:Expo.easeInOut,
        delay:-.7
     })
}

function cursoreffect(){
    // defining variables
    var xscale = 1
    var yscale = 1

    var xprev = 0
    var yprev = 0

    window.addEventListener("mousemove",function(dets){
        clearTimeout(timeout);
        xscale= gsap.utils.clamp(.8,1.2,dets.clientX - xprev)
        yscale = gsap.utils.clamp(.8,1.2,dets.clientY - yprev)

        xprev = dets.clientX
        yprev = dets.clientY

        cur(xscale,yscale)

        timeout = setTimeout(function(){
            document.querySelector(".cursor").style.transform = `translate(${dets.clientX}px,${dets.clientY}px) scale(1,1)`

        },100)
    });
}
cursoreffect();
function cur(xscale,yscale){
    window.addEventListener("mousemove",function(dets){
        document.querySelector(".cursor").style.transform = `translate(${dets.clientX}px,${dets.clientY}px) scale(${xscale},${yscale})`
    
    })
}
cur();
HPA();

document.querySelectorAll("#ele").forEach(function(ele){
    var rotate = 0;
    var diffrot = 0;
    ele.addEventListener("mousemove",function(dets){
        var diff = dets.clientY - ele.getBoundingClientRect();
        diffrot = dets.clientX - rotate
        rotate = dets.clientX
        console.log("hello ji")
        gsap.to(ele.querySelector("img"),{
            display:"block",
            opacity:1,
            top:diff,
            left:dets.clientX,
            rotate:gsap.utils.clamp(-20,20,diffrot)
            // ease:easeInOut,
        })
    })
})
