import { planetScaleEnum as scaleEnum } from './utility/scaling.mjs';
import {CLOCKWISE_TABLE, PLANET_FROM_NAME} from './utility/Planet.mjs';
import {Component, Color} from './utility/Util.mjs';
import { COMPONENT_WIDTH, IMAGE_HEIGHT, IMAGE_WIDTH, COMPONENT_HEIGHT } from './utility/scaling.mjs';

var config = {
	type: Phaser.AUTO,
	parent: 'phaser-example',
	width: 1200,
	height: 700,
	physics: {
		default: 'arcade',
		arcade: {
			debug: false,
			gravity: { y: 10 }
		}
	},
	scene: {
		preload: preload,
		create: create,
		update: update
	}
};

var game = new Phaser.Game(config);
var quantumCompSet = [];
var eventCardSet = [];
var image = [];

function preload() {
    this.load.image('bg', 'assets/BOARD1.png');
    this.load.atlas('quantumComp','assets/quantum_components/sprites.png','assets/quantum_components/quantumSprites.json');
    this.load.atlas('events','assets/event_cards/events.png','assets/event_cards/sprites.json');
}

function create() {
  this.socket = io();
  
  var bg = this.add.image(0,0,'bg').setOrigin(0,0);
  bg.displayWidth = config.width;
  bg.displayHeight = config.height;

  // TODO place engine cards and event cards faced down on their stacks

  /* Whenever an argument is received for which there is an enum in Utility,
  /  we need to do Enum_Name[argument] to obtain the correct value
  */

  this.socket.on('color', (color) => {
    var my_color = Color[color];
    // TODO assign the color to this player
  });

  this.socket.on('components', (component_map, blue_components, red_components) => {
    // component_map[i] is the component to be placed at scaleEnum[i]

    quantumCompSet = this.textures.get('quantumComp').getFrameNames();

    for (var i = 0; i < 8; ++i) {
      var comp = Component[component_map[i]]; // To get the component (which is basically the index in the image file)
      var planet_scale_values = scaleEnum[CLOCKWISE_TABLE[i].toJSON()];
      image[i] = this.add.sprite(planet_scale_values[0] * config.width, planet_scale_values[1] * config.height, 'quantumComp', quantumCompSet[comp]).setInteractive().setOrigin(0, 0);
      image[i].displayWidth = (COMPONENT_WIDTH / IMAGE_WIDTH) * config.width;
      image[i].displayHeight = (COMPONENT_HEIGHT / IMAGE_HEIGHT) * config.height;
    }

    // TODO : assign the player components using blue_components and red_components
  });

  this.socket.on('current_player', (curr_player_color) => {
    var color = Color[curr_player_color];
    // TODO : assign if it's this player's turn depending upon curr_player_color
  });

  this.socket.on('locations', (blue_location, red_location) => {
    var blue_planet = PLANET_FROM_NAME[blue_location];
    var red_planet = PLANET_FROM_NAME[red_location];

    // TODO : move the spaceships to their corresponding planets
  });

  this.socket.on('engine_decks', (blue, red) => {
    // TODO : update interface according to the decks received
  });

  this.socket.on('detection_rate', (rate) => {
    // TODO : update detection rate of the game
  });

  /*
  // creating and adding quantum components,event cards and engine cards all shuffles 
  this.socket.on('init', (quantumComponentIndices,eventIndices)=>{
    
    // creating and adding quantum components 
    quantumCompSet = this.textures.get('quantumComp').getFrameNames();
    let planets = quantumComponentIndices;
    for (var i = 0; i < 8; i++) {
      let currentValues = planets[i]
      image[i] = this.add.sprite(currentValues[0] * config.width, currentValues[1] * config.height, 'quantumComp', quantumCompSet[i]).setInteractive().setOrigin(0, 0);
      image[i].displayWidth = (97 / 1600) * config.width;
      image[i].displayHeight = (103 / 1200) * config.height;
    }

    //adding event cards 
    eventCardSet = this.textures.get('events').getFrameNames();
    let events = [(256/1600),(807/1200)];
    for (var i = 0; i < 10; i++) {
      image[i] = this.add.sprite(events[0] * config.width, events[1] * config.height, 'events', eventCardSet[i]).setInteractive().setOrigin(0, 0);
      image[i].displayWidth = (187 / 1600) * config.width;
      image[i].displayHeight = (274 / 1200) * config.height;
    }

  })*/


  /** 
  this.input.on('gameobjectover', function(pointer, draggableObject){
    draggableObject.setTint(0x000022);
  })

  this.input.on('gameobjectout',function(pointer,draggableObject){
    draggableObject.clearTint();
  })

  this.input.on('dragstart',function(pointer, draggableObject){
    draggableObject.setTint(0x110000);
  })

  this.input.on('drag',function(pointer, draggableObject, dragX, dragY){
    draggableObject.x = dragX;
    draggableObject.y = dragY;
  })

  this.input.on('dragend',function(pointer, draggableObject){
    draggableObject.clearTint();
  })
 
  var self = this;
  this.socket = io();
  this.background = this.add.image(0, 0, "background");
  this.background.setOrigin(0, 0);


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
  */ 
}

function update() {

}
