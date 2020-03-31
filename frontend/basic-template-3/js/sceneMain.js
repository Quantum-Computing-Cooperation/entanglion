class SceneMain extends Phaser.Scene {
    constructor() {
        super('SceneMain');
    }
    preload()
    {
        this.load.image("bg", "../gameAssets/bg.png");
        let galaxyMap = this.load.image("galaxyMap", "../gameAssets/transition-map.png");
        galaxyMap.width = 0.2;
    }
    create() {
        let bg = this.add.image(400,400,'bg');
        let galaxyMap = this.add.image(200,0,'galaxyMap');
        galaxyMap.width = 0.2;
        console.log("Ready!, working");
        this.aGrid = new AlignGrid({scene:this,rows:11,columns:11});
        this.aGrid.placeAtIndex(10,this.galaxyMap);
    }
    update() {}
}