var config = {
  type: Phaser.AUTO,
  parent: 'phaser-example',
  width: 800,
  height: 600,
  physics: {
    default: 'arcade',
    arcade: {
      debug: false,
      gravity: { y: 0 }
    }
  },
  scene: {
    preload: preload,
    create: create,
    update: update
  } 
};

var game = new Phaser.Game(config);

function preload() {

}

function create() {
  var self = this;
  this.socket = io();
  this.otherPlayers = this.physics.add.group();
  this.socket.on('component-map', function(data) {
    console.log(data);
  });
  this.socket.on('init_player', function(data) {
    console.log(data);
  });
  this.socket.on('locations', function(data1, data2) {
    console.log(data1, data2);
  });
  this.socket.on('engine_decks', function(one, two) {
    console.log(one, two);
  });
}

function update() {

}