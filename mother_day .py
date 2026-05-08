import streamlit as st
from streamlit.components.v1 import html

# 页面全屏，不显示任何 Streamlit 自带东西
st.set_page_config(
    page_title="母亲节快乐",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===================== 这里就是你的原版 HTML，一字未改 =====================
full_html = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>母亲节快乐</title>
<style>
html,body{
    height:100%;
    background:#000;
    overflow:hidden;
    margin:0;
    padding:0;
}
#child{
    position:fixed;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    z-index:9999;
}
h4{
    font-size:42px;
    color:#ff5e98;
    margin:0;
    font-family:Microsoft YaHei;
    font-weight:bold;
}
canvas{
    position:absolute;
    top:0;
    left:0;
    width:100%;
    height:100%;
}
#pinkboard{
    z-index:1;
}
.canvas{
    z-index:2;
}
</style>
</head>
<body>
<div id="child">
<h4>💗妈妈，母亲节快乐💗</h4>
</div>
<canvas id="pinkboard"></canvas>
<canvas class="canvas" id="canvas"></canvas>

<script>
!function(){for(n=0;n<400;n+=1)t=Math.random()*Math.PI*2,o=.1*Math.random()+1,e={x:160*Math.pow(Math.sin(t),3),y:130*Math.cos(t)-50*Math.cos(2*t)-20*Math.cos(3*t)-10*Math.cos(4*t)},e.x*=o,e.y*=o,e.vx=0,e.vy=0,e.pid=0,e.px=0,e.py=0,e.age=0,e.mtime=Math.random()*100+200,e.r=255,e.g=100+Math.random()*55,e.b=100+Math.random()*55,e.a=0,e.death=0,e.rands=Math.random()*1.5+0.5,e.f=1,e.s=1,i.push(e);for(n=0;n<400;n+=1)t=Math.random()*Math.PI*2,o=.1*Math.random()+1,e={x:160*Math.pow(Math.sin(t),3),y:130*Math.cos(t)-50*Math.cos(2*t)-20*Math.cos(3*t)-10*Math.cos(4*t)},e.x*=o,e.y*=o,e.vx=0,e.vy=0,e.pid=0,e.px=0,e.py=0,e.age=0,e.mtime=Math.random()*100+200,e.r=255,e.g=100+Math.random()*55,e.b=100+Math.random()*55,e.a=0,e.death=0,e.rands=Math.random()*1.5+0.5,e.f=1,e.s=0,i.push(e);a=document.getElementsByClassName("canvas")[0],c=a.getContext("2d"),o=document.getElementById("pinkboard"),n=o.getContext("2d"),a.width=window.innerWidth,a.height=window.innerHeight,o.width=window.innerWidth,o.height=window.innerHeight,window.onresize=function(){o.width=window.innerWidth,o.height=window.innerHeight,a.width=window.innerWidth,a.height=window.innerHeight},t=0,requestAnimationFrame(s);var i=[],e,t,o,a,c,n,h,r=Math.PI,d=function(t,o,e,i){c.beginPath(),c.moveTo(t,o),c.lineTo(e,i),c.stroke()},f=function(t,o,e,i,n){c.beginPath(),c.strokeStyle=i,c.fillStyle=e,c.lineWidth=n,c.arc(t,o,i,0,2*Math.PI),c.stroke(),c.fill()},s=function(){c.clearRect(0,0,a.width,a.height),n.clearRect(0,0,o.width,o.height),t+=1,t>360&&(t=0),h=10*Math.sin(t*Math.PI/180),r+=.04;for(eed=0;eed<i.length;eed+=1)x=i[eed],x.age++,x.age>x.mtime&&(x.death=1),x.px=x.x,x.py=x.y,x.vx*=x.f,x.vy*=x.f,x.vy+=.2,x.x+=x.vx,x.y+=x.vy,x.y+=h,x.rx=x.x,x.ry=x.y,x.x=160*Math.pow(Math.sin(t),3),x.y=130*Math.cos(t)-50*Math.cos(2*t)-20*Math.cos(3*t)-10*Math.cos(4*t),o*=x.rands,x.x*=x.rands,x.y*=x.rands,x.s==1&&(x.x+=a.width/2,x.y+=a.height/2),x.s==0&&(x.x+=o.width/2,x.y+=o.height/2),x.death==0?(x.a<1&&(x.a+=.04),x.pid==0?(d(x.px,x.py,x.rx,x.ry),x.pid=1):x.s==1?f(x.x,x.y,"rgba("+x.r+","+x.g+","+x.b+","+x.a+")",2,1):x.s==0&&f(x.x,x.y,"rgba("+x.r+","+x.g+","+x.b+","+x.a+")",2,1)):x.death==1&&(x.a>0?(x.a-=.05,x.s==1?f(x.x,x.y,"rgba("+x.r+","+x.g+","+x.b+","+x.a+")",2,1):x.s==0&&f(x.x,x.y,"rgba("+x.r+","+x.g+","+x.b+","+x.a+")",2,1)):(x.age=0,x.death=0,x.x=0,x.y=0,x.vx=Math.random()*6-3,x.vy=Math.random()*-6-2))}();
</script>

<script>
var canvas = document.getElementById("canvas"),
    ctx = canvas.getContext("2d"),
    w = canvas.width = window.innerWidth,
    h = canvas.height = window.innerHeight;
    str = "I LOVE YOU MOM ♥ 母亲节快乐",
    cols = Math.floor(w / 20) + 1,
    ypos = Array(cols).fill(0);
ctx.fillStyle = "#000";
ctx.fillRect(0, 0, w, h);
function matrix(){
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, w, h);
    ctx.fillStyle = "#ff5e98";
    ctx.font = "12pt monospace";
    ypos.forEach((y, ind) => {
        const text = str[Math.floor(Math.random() * str.length)];
        const x = ind * 20;
        ctx.fillText(text, x, y);
        if (y > 100 + Math.random() * 10000) ypos[ind] = 0;
        else ypos[ind] = y + 20;
    });
}
setInterval(matrix, 120);
</script>
</body>
</html>
"""

# ===================== 直接嵌入，1:1 还原你的原版效果 =====================
html(full_html, width=1200, height=800, scrolling=False)
