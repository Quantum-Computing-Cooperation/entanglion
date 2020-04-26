import { planetScaleEnum as scaleEnum } from './scaling.mjs';

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


function shuffle(arra1) {
	var ctr = arra1.length, temp, index;

	// While there are elements in the array
	while (ctr > 0) {
		// Pick a random index
		index = Math.floor(Math.random() * ctr);
		// Decrease ctr by 1
		ctr--;
		// And swap the last element with it
		temp = arra1[ctr];
		arra1[ctr] = arra1[index];
		arra1[index] = temp;
	}
	return arra1;
}

var game = new Phaser.Game(config);
var quantumCompSet = [];
var image = [];
let planets = shuffle(Object.values(scaleEnum).splice(1, 8));
console.log(planets);
var component_map = new Map();


function preload() {
	this.load.image('bg', 'assets/BOARD1.png');
	this.load.atlas('quantumComp', 'assets/quantum_components/sprites.png', 'assets/quantum_components/quantumSprites.json');
}

function create() {
	this.socket = io();
	var bg = this.add.image(0, 0, 'bg').setOrigin(0, 0);
	var draggableObject = this.add.group();
	bg.displayWidth = config.width;
	bg.displayHeight = config.height;
	quantumCompSet = this.textures.get('quantumComp').getFrameNames();

	image[0] = this.add.sprite((962 / 1600) * config.width, (262 / 1200) * config.height, 'quantumComp', quantumCompSet[i]).setInteractive().setOrigin(0, 0);
	image[0].displayWidth = (97 / 1600) * config.width;
	image[0].displayHeight = (103 / 1200) * config.height;

	// creating and adding quantum components 
	for (var i = 0; i < 8; i++) {
		let currentValues = planets[i]
		image[i] = this.add.sprite(currentValues[0] * config.width, currentValues[1] * config.height, 'quantumComp', quantumCompSet[i]).setInteractive().setOrigin(0, 0);
		image[i].displayWidth = (97 / 1600) * config.width;
		image[i].displayHeight = (103 / 1200) * config.height;
	}

	this.socket.on('components', function (rcvd_map, blue_comps, red_comps) {
		console.log('components received');
		component_map = new Map(JSON.parse(rcvd_map));
	});

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
