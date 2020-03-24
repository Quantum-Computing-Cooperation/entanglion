class Scene1 {
  constructor() {
    super("bootGame");
  }

  create() {
    this.add.text(20,20, "Loading game...");
    this.scene.start("playGame");
  }
}
