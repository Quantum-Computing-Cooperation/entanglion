class SceneMain extends Phaser.Scene {
    constructor() {
        super('SceneMain');
    }
    preload()
    {
        this.load.image("bg", "../gameAssets/board.jpg");
      
      
    }
    create() {

        /**
         *    // we first add background image
        let bg = this.add.image(0,0,'bg').setOrigin(0,0);
        bg.displayHeight = game.config.height;
        bg.displayWidth = game.config.width;
    
        // we define our main scene as consisting of 121 blocks 
        this.aGrid = new AlignGrid({scene:this,rows:11,columns:11});
        this.aGrid.placeAtIndex(40,this.galaxyMap);
         */

         //we define a grid where each object goes 
         this.aGrid = new AlignGrid({scene:this,rows:11,columns:2});
         
         this.aGrid.showNumbers();

        
        
    }
    update() {}
}