class Scene2 extends Phaser.Scene {
  constructor() {
    super("playGame");
  }

  create() {
    this.background = this.add.tileSprite(0, 0, this.game.config.width, this.game.config.height, "background");
    this.background.setOrigin(0, 0);

    this.ship1 = this.add.sprite(this.game.config.width / 2 - 50, this.game.config.height / 2, "ship");
    this.ship2 = this.add.sprite(this.game.config.width / 2, this.game.config.height / 2, "ship2");
    this.ship3 = this.add.sprite(this.game.config.width / 2 + 50, this.game.config.height / 2, "ship3");

    this.anims.create({
      key: "ship1_anim",
      frames: this.anims.generateFrameNumbers("ship"),
      frameRate: 20,
      repeat: -1
    });
    this.anims.create({
      key: "ship2_anim",
      frames: this.anims.generateFrameNumbers("ship2"),
      frameRate: 20,
      repeat: -1
    });
    this.anims.create({
      key: "ship3_anim",
      frames: this.anims.generateFrameNumbers("ship3"),
      frameRate: 20,
      repeat: -1
    });
    this.anims.create({
      key: "explode",
      frames: this.anims.generateFrameNumbers("explosion"),
      frameRate: 20,
      repeat: 0,
      hideOnComplete: true
    });

    this.ship1.play("ship1_anim");
    this.ship2.play("ship2_anim");
    this.ship3.play("ship3_anim");

    this.ship1.setInteractive();
    this.ship2.setInteractive();
    this.ship3.setInteractive();

    this.input.on('gameobjectdown', this.destroyShip, this);
  }

  update() {

    this.moveShip(this.ship1, 1);
    this.moveShip(this.ship2, 2);
    this.moveShip(this.ship3, 3);

    this.background.tilePositionY -= 0.5;

  }


  moveShip(ship, speed) {
    // increase the position of the ship on the vertical axis
    ship.y += speed;
    // if the ship hits the bottom of the screen call the reset function
    if (ship.y > this.game.config.height) {
      // call a reset position function
      this.resetShipPos(ship);
    }
  }

  // create the reset position function
  resetShipPos(ship){
    // put the ship on the top
    ship.y = 0;
    // put the ship on a random position on the x axis
    var randomX = Phaser.Math.Between(0, this.game.config.width);
    ship.x = randomX;
  }

  destroyShip(pointer, gameObject){
    gameObject.setTexture("explosion");
    gameObject.play("explode");
   }


}
