class SceneMain extends Phaser.Scene {
    constructor() {
        super('SceneMain');
    }
    preload()
    {
        this.load.image("bg", "assets/BOARD1.png");
    }

    create() {

        // we first add background image
        this.bg = this.add.image(0,0,"bg").setOrigin(0,0);
        this.bg.displayHeight = game.config.height;
        this.bg.displayWidth = game.config.width;

        // we define our main scene as consisting of 121 blocks
      //  this.aGrid = new AlignGrid({scene:this,rows:11,columns:11});
        //this.aGrid.placeAtIndex(40,this.galaxyMap);

         //we define a grid where each object goes
      //   this.aGrid = new AlignGrid({scene:this,rows:11,columns:2});

      //   this.aGrid.showNumbers();
      var self = this;
      this.socket = io();
      this.background = this.add.image(0, 0, "background");
      this.background.setOrigin(0, 0);


      this.socket.on('component_map', function(data) {
        console.log('component map received');
        var map = new Map(JSON.parse(data));
        map.forEach((key, value) => console.log(key + '=' + value));
      });
      this.socket.on('player', function(data) {
        console.log('init player done it is: ', data);
      });
      this.socket.on('locations', function(data1, data2) {
        console.log('locations: ', data1, data2);
      });
      this.socket.on('engine_decks', function(one, two) {
        console.log('engine deck 1: ', one, '\n engine deck 2: ', two);
      });


    }
    update() {}
}
