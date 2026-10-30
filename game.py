
from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VOID RUNNER | Dino Survival</title>

<style>
* { margin:0; padding:0; box-sizing:border-box; }

:root {
    --cyan: #69f5ff;
    --white: #f3fbff;
    --muted: #8ba5b8;
}

body {
    background:#03070d;
    color:var(--white);
    font-family: "Segoe UI", Arial, sans-serif;
    min-height:100vh;
    display:grid;
    place-items:center;
    overflow:hidden;
}

.game-shell {
    position:relative;
    width:min(1100px, 96vw);
    border:1px solid #243c4b;
    background:#06101b;
    box-shadow:0 0 80px #00d9ff12, 0 30px 100px #000;
    overflow:hidden;
}

.topbar {
    height:76px;
    padding:0 30px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    border-bottom:1px solid #203744;
    background:#07111beF;
    position:relative;
    z-index:2;
}

.brand {
    font-size:15px;
    font-weight:800;
    letter-spacing:4px;
}

.brand span { color:var(--cyan); }

.status {
    font-size:10px;
    letter-spacing:2px;
    color:#8ba5b8;
}

.status i {
    display:inline-block;
    width:7px;
    height:7px;
    background:#72ffba;
    border-radius:50%;
    margin-right:8px;
    box-shadow:0 0 12px #72ffba;
}

.stats { display:flex; gap:35px; }

.stat-label {
    font-size:9px;
    letter-spacing:2px;
    color:#8298a8;
    margin-bottom:5px;
}

.stat-value {
    font-size:22px;
    font-weight:700;
    letter-spacing:2px;
}

#score { color:var(--cyan); }

.scene {
    position:relative;
    height:490px;
    background:linear-gradient(180deg,#07152b 0%,#102943 52%,#253e50 100%);
    overflow:hidden;
}

.scene:after {
    content:"";
    position:absolute;
    inset:0;
    pointer-events:none;
    z-index:1;
    background:linear-gradient(90deg,#02071166,transparent 30%,transparent 75%,#02071155);
}

.moon {
    position:absolute;
    width:85px;
    height:85px;
    border-radius:50%;
    top:60px;
    right:18%;
    background:#e6fbff;
    box-shadow:0 0 25px #b8f4ff99, 0 0 100px #62cfff44;
}

.moon:after {
    content:"";
    position:absolute;
    inset:0;
    border-radius:50%;
    background:linear-gradient(120deg,transparent 30%,#a3d0eb55);
}

.stars {
    position:absolute;
    inset:0;
    background-image:
      radial-gradient(2px 2px at 10% 20%,#fff 99%,transparent),
      radial-gradient(1px 1px at 25% 12%,#fff 99%,transparent),
      radial-gradient(2px 2px at 43% 30%,#fff 99%,transparent),
      radial-gradient(1px 1px at 65% 15%,#fff 99%,transparent),
      radial-gradient(2px 2px at 78% 35%,#fff 99%,transparent),
      radial-gradient(1px 1px at 91% 10%,#fff 99%,transparent),
      radial-gradient(1px 1px at 14% 42%,#fff 99%,transparent),
      radial-gradient(1px 1px at 55% 8%,#fff 99%,transparent),
      radial-gradient(2px 2px at 35% 45%,#fff 99%,transparent);
}

.mountains {
    position:absolute;
    bottom:95px;
    left:0;
    width:200%;
    height:220px;
    opacity:.55;
    background:#102536;
    clip-path:polygon(0 80%,8% 30%,15% 70%,23% 12%,32% 73%,
      41% 32%,50% 75%,59% 20%,68% 78%,78% 25%,88% 70%,95% 38%,
      100% 75%,100% 100%,0 100%);
}

.mountains.far {
    bottom:110px;
    opacity:.45;
    transform:translateX(30px) scaleY(.7);
    background:#315064;
}

.ground {
    position:absolute;
    bottom:0;
    width:100%;
    height:95px;
    background:linear-gradient(180deg,#172c39,#08131d);
    border-top:2px solid #6df4ff;
    box-shadow:0 -6px 28px #2ee9ff18;
}

.ground:before {
    content:"";
    position:absolute;
    inset:10px 0 0;
    opacity:.35;
    background:repeating-linear-gradient(90deg,
      transparent 0 35px,#4adce4 36px,#4adce4 37px,transparent 38px 70px);
    transform:perspective(120px) rotateX(25deg);
}

.horizon {
    position:absolute;
    bottom:96px;
    width:100%;
    height:1px;
    box-shadow:0 0 25px 3px #56eaff44;
}

canvas {
    position:absolute;
    inset:0;
    width:100%;
    height:100%;
    z-index:1;
}

.overlay {
    position:absolute;
    inset:0;
    z-index:3;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    text-align:center;
    padding:20px;
    background:linear-gradient(90deg,#06101b55,#06101b22,#06101b55);
    transition:opacity .25s;
}

.overlay.hidden {
    opacity:0;
    pointer-events:none;
}

.eyebrow {
    color:var(--cyan);
    font-size:10px;
    letter-spacing:5px;
    margin-bottom:18px;
}

.overlay h1 {
    font-size:clamp(38px,7vw,75px);
    line-height:1;
    letter-spacing:4px;
    font-weight:900;
    text-shadow:0 0 35px #49e9ff44;
}

.overlay h1 span { color:var(--cyan); }

.subtitle {
    margin-top:20px;
    color:#b4c9d7;
    font-size:13px;
    line-height:1.8;
    letter-spacing:1px;
}

.play-btn {
    margin-top:28px;
    border:1px solid var(--cyan);
    padding:15px 34px;
    background:#58edff12;
    color:white;
    font-size:11px;
    font-weight:800;
    letter-spacing:3px;
    cursor:pointer;
    transition:.25s;
}

.play-btn:hover {
    background:var(--cyan);
    color:#041019;
    box-shadow:0 0 35px #53edff66;
    transform:translateY(-2px);
}

.controls {
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:15px;
    padding:18px 28px;
    background:#07111b;
    border-top:1px solid #203744;
}

.hint {
    color:#7892a5;
    font-size:10px;
    letter-spacing:1px;
    line-height:1.8;
}

kbd {
    color:#e6faff;
    border:1px solid #426170;
    background:#122430;
    padding:4px 9px;
    margin-right:5px;
    border-radius:3px;
}

.mobile-btn {
    display:none;
    padding:12px 20px;
    border:1px solid var(--cyan);
    background:#0c2634;
    color:white;
    font-size:11px;
    letter-spacing:2px;
    cursor:pointer;
}

.scanlines {
    position:absolute;
    inset:0;
    z-index:4;
    pointer-events:none;
    opacity:.12;
    background:repeating-linear-gradient(
      0deg,transparent 0 3px,#000 4px,transparent 5px
    );
}

.footer {
    display:flex;
    justify-content:space-between;
    padding:13px 28px;
    color:#526b7b;
    font-size:9px;
    letter-spacing:2px;
    background:#050b12;
}

@media(max-width:600px) {
    .topbar { padding:0 15px; height:65px; }
    .brand { font-size:12px; letter-spacing:2px; }
    .stats { gap:15px; }
    .stat-value { font-size:17px; }
    .status { display:none; }
    .scene { height:65vh; min-height:400px; max-height:490px; }
    .controls { padding:14px; }
    .hint { font-size:9px; }
    .mobile-btn { display:block; }
    .footer { padding:12px; font-size:8px; }
    .moon { width:60px; height:60px; }
}
</style>
</head>

<body>
<div class="game-shell">

    <header class="topbar">
        <div class="brand">VOID <span>RUNNER</span></div>
        <div class="status"><i></i>SURVIVAL SYSTEM ONLINE</div>
        <div class="stats">
            <div>
                <div class="stat-label">SCORE</div>
                <div class="stat-value" id="score">00000</div>
            </div>
            <div>
                <div class="stat-label">BEST</div>
                <div class="stat-value" id="best">00000</div>
            </div>
        </div>
    </header>

    <main class="scene" id="scene">
        <div class="stars"></div>
        <div class="moon"></div>
        <div class="mountains far"></div>
        <div class="mountains"></div>
        <div class="ground"></div>
        <div class="horizon"></div>
        <canvas id="game"></canvas>

        <div class="overlay" id="overlay">
            <div class="eyebrow" id="eyebrow">A CINEMATIC SURVIVAL EXPERIENCE</div>
            <h1 id="headline">VOID <span>RUNNER</span></h1>
            <p class="subtitle" id="message">
                THE WORLD WENT DARK.<br>
                YOUR SURVIVAL STARTS NOW.
            </p>
            <button class="play-btn" id="play">▶ &nbsp; START RUN</button>
        </div>

        <div class="scanlines"></div>
    </main>

    <section class="controls">
        <div class="hint">
            <kbd>SPACE</kbd> <kbd>↑</kbd> JUMP
            &nbsp; / &nbsp; <kbd>↓</kbd> DUCK
            <br>AVOID OBSTACLES. SURVIVE THE NIGHT.
        </div>
        <button class="mobile-btn" id="jump">TAP TO JUMP ↗</button>
        <div class="hint">MODE: ENDLESS</div>
    </section>

    <footer class="footer">
        <span>VOID RUNNER / 001</span>
        <span>BUILT FOR THE NIGHT</span>
    </footer>

</div>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const scene = document.getElementById("scene");
const overlay = document.getElementById("overlay");
const playBtn = document.getElementById("play");
const jumpBtn = document.getElementById("jump");

let W = 1000, H = 490, groundY = 395;
let running = false, gameOver = false;
let lastTime = 0, score = 0, speed = 6;
let obstacles = [], particles = [], dust = [];
let spawnTimer = 0, animationTime = 0;
let ducking = false;
let best = 0;

try {
    best = Number(localStorage.getItem("voidRunnerBest")) || 0;
} catch(e) {}

document.getElementById("best").textContent =
    String(best).padStart(5, "0");

const dino = {
    x: 100, y: 0, vy: 0, w: 42, h: 50,
    grounded: true, leg: 0
};

function resize() {
    const rect = scene.getBoundingClientRect();
    const oldH = H;
    W = rect.width;
    H = rect.height;
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(W * dpr);
    canvas.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    groundY = H - 95;
    if (dino.grounded || dino.y === 0) {
        dino.y = groundY - dino.h;
    } else {
        dino.y = Math.min(groundY - dino.h, dino.y + (H-oldH));
    }
    dino.x = Math.max(45, Math.min(100, W * .11));
}
window.addEventListener("resize", resize);
resize();

function reset() {
    score = 0;
    speed = 6;
    spawnTimer = 0;
    obstacles = [];
    particles = [];
    ducking = false;
    dino.h = 50;
    dino.y = groundY - dino.h;
    dino.vy = 0;
    dino.grounded = true;
    dino.leg = 0;
    gameOver = false;
    running = true;
    lastTime = 0;
    overlay.classList.add("hidden");
    document.getElementById("score").textContent = "00000";
    requestAnimationFrame(loop);
}

function jump() {
    if (!running) {
        if (gameOver) reset();
        else reset();
        return;
    }

    if (dino.grounded && !ducking) {
        dino.vy = -15;
        dino.grounded = false;
        for (let i=0; i<8; i++) {
            particles.push({
                x:dino.x+12, y:groundY-3,
                vx:(Math.random()-.5)*4,
                vy:-Math.random()*3,
                life:1
            });
        }
    }
}

function endGame() {
    running = false;
    gameOver = true;
    ducking = false;

    if (Math.floor(score) > best) {
        best = Math.floor(score);
        try {
            localStorage.setItem("voidRunnerBest", best);
        } catch(e) {}
    }

    document.getElementById("best").textContent =
        String(best).padStart(5, "0");

    document.getElementById("eyebrow").textContent =
        "SURVIVAL SEQUENCE TERMINATED";
    document.getElementById("headline").innerHTML =
        'GAME <span>OVER</span>';
    document.getElementById("message").innerHTML =
        "YOU SURVIVED " + Math.floor(score) +
        " METERS.<br>THE NIGHT IS NOT OVER.";
    playBtn.innerHTML = "↻ &nbsp; TRY AGAIN";
    overlay.classList.remove("hidden");

    for (let i=0; i<24; i++) {
        particles.push({
            x:dino.x+20, y:dino.y+20,
            vx:(Math.random()-.5)*9,
            vy:(Math.random()-.5)*9,
            life:1
        });
    }
}

function startScreen() {
    running = false;
    gameOver = false;
    dino.y = groundY - dino.h;
    draw();
}
playBtn.addEventListener("click", jump);
jumpBtn.addEventListener("click", jump);

window.addEventListener("keydown", e => {
    if (["Space","ArrowUp","ArrowDown"].includes(e.code)) {
        e.preventDefault();
    }
    if (e.repeat) return;

    if (e.code === "Space" || e.code === "ArrowUp") jump();
    if (e.code === "ArrowDown" && running) ducking = true;
    if (e.code === "KeyR" && gameOver) reset();
});
window.addEventListener("keyup", e => {
    if (e.code === "ArrowDown") ducking = false;
});

canvas.addEventListener("pointerdown", e => {
    if (e.pointerType === "touch") jump();
});

function drawDino() {
    const x = dino.x;
    const y = dino.y;
    const h = ducking && dino.grounded ? 29 : dino.h;
    const w = ducking && dino.grounded ? 53 : dino.w;
    const dy = dino.h - h;
    const run = Math.sin(dino.leg) * 8;

    ctx.save();
    ctx.translate(x, y+dy);

    // Neon aura
    ctx.shadowBlur = 18;
    ctx.shadowColor = "#64f5ff";
    ctx.fillStyle = "#b5fbff";

    if (ducking && dino.grounded) {
        ctx.fillRect(3, 9, 38, 19);
        ctx.fillRect(31, 1, 18, 17);
        ctx.fillRect(42, 4, 5, 5);
        ctx.fillStyle = "#071523";
        ctx.fillRect(42, 5, 3, 3);
        ctx.shadowBlur = 0;
        ctx.fillStyle = "#64f5ff";
        ctx.fillRect(10, 24, 7, 8);
        ctx.fillRect(31, 24, 7, 8);
    } else {
        // Tail, body and head
        ctx.fillRect(0, 22, 13, 7);
        ctx.fillRect(10, 13, 23, 27);
        ctx.fillRect(23, 0, 21, 22);
        ctx.fillRect(37, 14, 12, 7);
        ctx.fillRect(17, 18, 8, 13);

        ctx.shadowBlur = 0;
        ctx.fillStyle = "#06131e";
        ctx.fillRect(37, 5, 4, 4);

        ctx.fillStyle = "#72edff";
        if (dino.grounded) {
            ctx.fillRect(13, 38, 7, 12+run);
            ctx.fillRect(27, 38, 7, 12-run);
        } else {
            ctx.fillRect(13, 39, 7, 8);
            ctx.fillRect(27, 39, 7, 8);
        }

        // Chest light
        ctx.fillStyle = "#fff";
        ctx.globalAlpha = .8;
        ctx.fillRect(17, 22, 3, 7);
    }
    ctx.restore();
}

function drawCactus(o) {
    ctx.save();
    ctx.translate(o.x, groundY);
    ctx.shadowBlur = 12;
    ctx.shadowColor = "#55ffbd";
    ctx.fillStyle = "#57e8ad";

    if (o.type === 0) {
        ctx.fillRect(0,-o.h,14,o.h);
        ctx.fillRect(-8,-o.h+15,8,7);
        ctx.fillRect(-8,-o.h+8,5,14);
        ctx.fillRect(14,-o.h+24,9,7);
        ctx.fillRect(18,-o.h+16,5,15);
    } else if (o.type === 1) {
        ctx.fillRect(0,-o.h,12,o.h);
        ctx.fillRect(-8,-o.h+11,8,6);
        ctx.fillRect(-8,-o.h+4,5,13);
    } else {
        ctx.fillRect(0,-o.h,22,o.h);
        ctx.fillRect(-10,-o.h+15,10,8);
        ctx.fillRect(-10,-o.h+8,5,15);
        ctx.fillRect(22,-o.h+24,10,8);
        ctx.fillRect(27,-o.h+15,5,18);
    }
    ctx.restore();
}

function draw() {
    ctx.clearRect(0,0,W,H);

    // Atmospheric horizon glow
    const glow = ctx.createRadialGradient(
        W*.65, groundY, 0, W*.65, groundY, W*.6
    );
    glow.addColorStop(0,"#20dfff14");
    glow.addColorStop(1,"#20dfff00");
    ctx.fillStyle = glow;
    ctx.fillRect(0,0,W,H);

    // Moving ground lights
    ctx.save();
    ctx.strokeStyle = "#55edff44";
    ctx.lineWidth = 1;
    const offset = (animationTime*speed*.6)%65;
    for (let x=-65-offset; x<W+65; x+=65) {
        ctx.beginPath();
        ctx.moveTo(x,groundY+15);
        ctx.lineTo(x+18,groundY+15);
        ctx.stroke();
    }
    ctx.restore();

    // Distant tiny glowing lights
    for (let i=0;i<8;i++) {
        const x = ((i*173-animationTime*speed*.18)%(W+40)+W+40)%(W+40);
        ctx.fillStyle = "#76f3ff77";
        ctx.fillRect(x,groundY-70-(i%3)*25,2,2);
    }

    obstacles.forEach(drawCactus);
    drawDino();

    particles.forEach(p => {
        ctx.globalAlpha = Math.max(0,p.life);
        ctx.fillStyle = "#75f5ff";
        ctx.fillRect(p.x,p.y,3,3);
    });
    ctx.globalAlpha = 1;
}

function loop(timestamp) {
    if (!running) return;
    const dt = lastTime ? Math.min((timestamp-lastTime)/16.67,2) : 1;
    lastTime = timestamp;
    animationTime += dt;

    speed = Math.min(14, 6 + score/500);
    score += dt * speed * .12;
    document.getElementById("score").textContent =
        String(Math.floor(score)).padStart(5,"0");

    dino.leg += .22*dt*speed/6;

    // Jump physics
    if (!dino.grounded) {
        dino.vy += .72*dt;
        dino.y += dino.vy*dt;

        if (dino.y >= groundY-dino.h) {
            dino.y = groundY-dino.h;
            dino.vy = 0;
            dino.grounded = true;
        }
    }

    // Spawn obstacles
    spawnTimer -= dt;
    if (spawnTimer <= 0) {
        const height = 30 + Math.random()*30;
        obstacles.push({
            x:W+30,
            h:height,
            type:Math.floor(Math.random()*3),
            w:32
        });
        spawnTimer = 75 + Math.random()*45;
        spawnTimer *= Math.max(.62, 1-score/4000);
    }

    obstacles.forEach(o => {
        o.x -= speed*dt;

        // Slightly forgiving collision box
        const dh = ducking ? 25 : 39;
        const dy = dino.y + (dino.h-dh);
        const dx = dino.x + 7;
        const dw = ducking ? 39 : 29;
        const ox = o.x + 2;
        const ow = o.type === 2 ? 27 : 18;
        const oy = groundY-o.h+3;

        if (dx+dw > ox && dx < ox+ow &&
            dy+dh > oy && dy < groundY) {
            endGame();
        }
    });
    obstacles = obstacles.filter(o=>o.x>-70);

    particles.forEach(p => {
        p.x += p.vx*dt;
        p.y += p.vy*dt;
        p.vy += .12*dt;
        p.life -= .025*dt;
    });
    particles = particles.filter(p=>p.life>0);

    draw();
    if (running) requestAnimationFrame(loop);
}

function idleLoop(timestamp) {
    if (!running) {
        animationTime += .35;
        draw();
        requestAnimationFrame(idleLoop);
    }
}
startScreen();
requestAnimationFrame(idleLoop);
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
