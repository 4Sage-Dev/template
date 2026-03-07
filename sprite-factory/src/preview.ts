import { Application, Assets, AnimatedSprite, Texture, Rectangle, Container, Sprite } from 'pixi.js';

async function initPreview() {
    const container = document.getElementById('preview-container');
    if (!container) return;
    const app = new Application();
    await app.init({ 
        width: container.clientWidth || 600, 
        height: container.clientHeight || 500, 
        backgroundColor: 0xFFFFFF, // WHITE BACKGROUND
        antialias: false, 
        resizeTo: container 
    });
    container.appendChild(app.canvas);

    // 1. THE ASSET MAP (Add new sprites here)
    const assetMap: Record<string, string> = {
        example: '/assets/example/sprite.png'
    };

    const loaded: any = {};
    for (const [key, path] of Object.entries(assetMap)) {
        try { loaded[key] = await Assets.load(path); } catch(e) { console.error("Load failed:", path); }
    }

    // 2. EXTRACTION HELPER
    const extract = (tex: any, count: number, size: number = 32) => {
        if (!tex) return [];
        const f = [];
        for(let i = 0; i < count; i++) f.push(new Texture({ source: tex.source, frame: new Rectangle(i * size, 0, size, size) }));
        return f;
    };

    // 3. FRAME REGISTRY
    const frames = {
        example: extract(loaded.example, 3)
    };

    // 4. SIMULATION OBJECTS
    if (frames.example.length > 0) {
        const sample = new AnimatedSprite(frames.example);
        sample.anchor.set(0.5);
        sample.x = app.screen.width / 2;
        sample.y = app.screen.height / 2;
        sample.animationSpeed = 0.1;
        sample.play();
        app.stage.addChild(sample);
    }

    app.ticker.add((ticker) => {
        // Animation updates happen here
    });
}
initPreview();
