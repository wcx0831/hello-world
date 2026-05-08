import streamlit as st
from streamlit.components.v1 import html

# 整理后的HTML/JS代码（单根节点、修复语法、移除无效依赖）
love_html = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>母亲节快乐</title>
    <style>
        html,
        body {
            height: 100%;
            padding: 0;
            margin: 0;
            background: rgb(0, 0, 0);
            overflow: hidden;
        }
        #child {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 10000;
        }
        h4 {
            font-family: "STKaiti", "KaiTi", serif;
            font-size: 40px;
            color: #943e4e;
            margin: 0;
        }
        canvas {
            position: absolute;
            width: 100%;
            height: 100%;
        }
        #pinkboard {
            z-index: 1;
        }
        .canvas {
            z-index: 2;
        }
    </style>
</head>
<body>
    <div id="child">
        <h4>💗妈妈，节日快乐</h4>
    </div>
    <canvas id="pinkboard"></canvas>
    <canvas class="canvas" id="canvas"></canvas>

    <script>
        // 1. 爱心粒子效果
        var settings = {
            particles: {
                length: 500,
                duration: 2,
                velocity: 100,
                effect: -0.75,
                size: 30,
            },
        };

        // RequestAnimationFrame兼容
        (function () {
            var b = 0;
            var c = ["ms", "moz", "webkit", "o"];
            for (var a = 0; a < c.length && !window.requestAnimationFrame; ++a) {
                window.requestAnimationFrame = window[c[a] + "RequestAnimationFrame"];
                window.cancelAnimationFrame = window[c[a] + "CancelAnimationFrame"] || window[c[a] + "CancelRequestAnimationFrame"];
            }
            if (!window.requestAnimationFrame) {
                window.requestAnimationFrame = function (h, e) {
                    var d = new Date().getTime();
                    var f = Math.max(0, 16 - (d - b));
                    var g = window.setTimeout(function () { h(d + f) }, f);
                    b = d + f;
                    return g;
                };
            }
            if (!window.cancelAnimationFrame) {
                window.cancelAnimationFrame = function (d) { clearTimeout(d); };
            }
        })();

        // Point类
        var Point = (function () {
            function Point(x, y) {
                this.x = (typeof x !== 'undefined') ? x : 0;
                this.y = (typeof y !== 'undefined') ? y : 0;
            }
            Point.prototype.clone = function () {
                return new Point(this.x, this.y);
            };
            Point.prototype.length = function (length) {
                if (typeof length == 'undefined')
                    return Math.sqrt(this.x * this.x + this.y * this.y);
                this.normalize();
                this.x *= length;
                this.y *= length;
                return this;
            };
            Point.prototype.normalize = function () {
                var length = this.length();
                this.x /= length;
                this.y /= length;
                return this;
            };
            return Point;
        })();

        // Particle类
        var Particle = (function () {
            function Particle() {
                this.position = new Point();
                this.velocity = new Point();
                this.acceleration = new Point();
                this.age = 0;
            }
            Particle.prototype.initialize = function (x, y, dx, dy) {
                this.position.x = x;
                this.position.y = y;
                this.velocity.x = dx;
                this.velocity.y = dy;
                this.acceleration.x = dx * settings.particles.effect;
                this.acceleration.y = dy * settings.particles.effect;
                this.age = 0;
            };
            Particle.prototype.update = function (deltaTime) {
                this.position.x += this.velocity.x * deltaTime;
                this.position.y += this.velocity.y * deltaTime;
                this.velocity.x += this.acceleration.x * deltaTime;
                this.velocity.y += this.acceleration.y * deltaTime;
                this.age += deltaTime;
            };
            Particle.prototype.draw = function (context, image) {
                function ease(t) {
                    return (--t) * t * t + 1;
                }
                var size = image.width * ease(this.age / settings.particles.duration);
                context.globalAlpha = 1 - this.age / settings.particles.duration;
                context.drawImage(image, this.position.x - size / 2, this.position.y - size / 2, size, size);
            };
            return Particle;
        })();

        // ParticlePool类
        var ParticlePool = (function () {
            var particles,
                firstActive = 0,
                firstFree = 0,
                duration = settings.particles.duration;

            function ParticlePool(length) {
                particles = new Array(length);
                for (var i = 0; i < particles.length; i++)
                    particles[i] = new Particle();
            }
            ParticlePool.prototype.add = function (x, y, dx, dy) {
                particles[firstFree].initialize(x, y, dx, dy);
                firstFree++;
                if (firstFree == particles.length) firstFree = 0;
                if (firstActive == firstFree) firstActive++;
                if (firstActive == particles.length) firstActive = 0;
            };
            ParticlePool.prototype.update = function (deltaTime) {
                var i;
                if (firstActive < firstFree) {
                    for (i = firstActive; i < firstFree; i++)
                        particles[i].update(deltaTime);
                }
                if (firstFree < firstActive) {
                    for (i = firstActive; i < particles.length; i++)
                        particles[i].update(deltaTime);
                    for (i = 0; i < firstFree; i++)
                        particles[i].update(deltaTime);
                }
                while (particles[firstActive].age >= duration && firstActive != firstFree) {
                    firstActive++;
                    if (firstActive == particles.length) firstActive = 0;
                }
            };
            ParticlePool.prototype.draw = function (context, image) {
                var i;
                if (firstActive < firstFree) {
                    for (i = firstActive; i < firstFree; i++)
                        particles[i].draw(context, image);
                }
                if (firstFree < firstActive) {
                    for (i = firstActive; i < particles.length; i++)
                        particles[i].draw(context, image);
                    for (i = 0; i < firstFree; i++)
                        particles[i].draw(context, image);
                }
            };
            return ParticlePool;
        })();

        // 渲染爱心
        function renderLove(canvas) {
            var context = canvas.getContext('2d'),
                particles = new ParticlePool(settings.particles.length),
                particleRate = settings.particles.length / settings.particles.duration,
                time;

            function pointOnHeart(t) {
                return new Point(
                    160 * Math.pow(Math.sin(t), 3),
                    130 * Math.cos(t) - 50 * Math.cos(2 * t) - 20 * Math.cos(3 * t) - 10 * Math.cos(4 * t) + 25
                );
            }

            // 创建粒子图片
            var image = (function () {
                var canvas = document.createElement('canvas'),
                    context = canvas.getContext('2d');
                canvas.width = settings.particles.size;
                canvas.height = settings.particles.size;
                function to(t) {
                    var point = pointOnHeart(t);
                    point.x = settings.particles.size / 2 + point.x * settings.particles.size / 350;
                    point.y = settings.particles.size / 2 - point.y * settings.particles.size / 350;
                    return point;
                }
                context.beginPath();
                var t = -Math.PI;
                var point = to(t);
                context.moveTo(point.x, point.y);
                while (t < Math.PI) {
                    t += 0.01;
                    point = to(t);
                    context.lineTo(point.x, point.y);
                }
                context.closePath();
                context.fillStyle = '#943e4e';
                context.fill();
                var image = new Image();
                image.src = canvas.toDataURL();
                return image;
            })();

            function render() {
                requestAnimationFrame(render);
                var newTime = new Date().getTime() / 1000,
                    deltaTime = newTime - (time || newTime);
                time = newTime;

                context.clearRect(0, 0, canvas.width, canvas.height);

                var amount = particleRate * deltaTime;
                for (var i = 0; i < amount; i++) {
                    var pos = pointOnHeart(Math.PI - 2 * Math.PI * Math.random());
                    var dir = pos.clone().length(settings.particles.velocity);
                    particles.add(canvas.width / 2 + pos.x, canvas.height / 2 - pos.y, dir.x, -dir.y);
                }

                particles.update(deltaTime);
                particles.draw(context, image);
            }

            function onResize() {
                canvas.width = canvas.clientWidth;
                canvas.height = canvas.clientHeight;
            }
            window.onresize = onResize;

            setTimeout(function () {
                onResize();
                render();
            }, 10);
        }

        // 2. 字符雨效果
        function renderCharRain() {
            var canvas = document.getElementById('canvas');
            var ctx = canvas.getContext('2d');
            canvas.height = window.innerHeight;
            canvas.width = window.innerWidth;

            var texts = 'I LOVE Y'.split('');
            var fontSize = 16;
            var columns = canvas.width / fontSize;
            var drops = [];
            for (var x = 0; x < columns; x++) {
                drops[x] = 1;
            }

            function draw() {
                ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = '#943e4e';
                ctx.font = fontSize + 'px arial';
                for (var i = 0; i < drops.length; i++) {
                    var text = texts[Math.floor(Math.random() * texts.length)];
                    ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                    if (drops[i] * fontSize > canvas.height || Math.random() > 0.95) {
                        drops[i] = 0;
                    }
                    drops[i]++;
                }
            }
            setInterval(draw, 33);
        }

        // 初始化
        window.onload = function () {
            // 渲染爱心粒子
            renderLove(document.getElementById('pinkboard'));
            // 渲染字符雨
            renderCharRain();
            // 显示祝福语（可选：添加淡入效果）
            setTimeout(() => {
                document.getElementById('child').style.opacity = 1;
            }, 500);
        };
    </script>
</body>
</html>
"""

# Streamlit页面配置
st.set_page_config(
    page_title="母亲节快乐",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 嵌入HTML（设置高度为100vh占满屏幕）
html(love_html, height=800, scrolling=False)
