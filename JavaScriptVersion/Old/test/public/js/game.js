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
  this.socket.on('component_map', function(data) {
    console.log('component map received');
    var map = new Map(JSON.parse(data));
    for([key,value] of map)
      console.log(key + '=' + value);
  });
  this.socket.on('init_player', function(data) {
    console.log('inti player done it is: ', data);
  });
  this.socket.on('locations', function(data1, data2) {
    console.log('locations: ', data1, data2);
  });
  this.socket.on('engine_decks', function(one, two) {
    console.log('engine deck 1: ', one, '\n engine deck 2: ', two);
  });
}

function update() {

}
