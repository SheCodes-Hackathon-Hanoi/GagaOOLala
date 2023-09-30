<template>
  <div id="panorama-container"></div>
</template>

<script>
export default {
  props: {
    imageSource: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
    };
  },
  mounted() {
    this.init();
  },
  methods: {
    init() {
      // Create a new camera object
      this.camera = new THREE.PerspectiveCamera(
        100,
        window.innerWidth / window.innerHeight,
        1,
        1000
      );

      // Set the camera position
      this.camera.position.set(0, 0, 0.1);

      // Create a new scene object
      this.scene = new THREE.Scene();

      // Load the panorama image
      const loader = new THREE.TextureLoader();
      const texture = loader.load(this.imageSource);

      // Set the texture wrapping and flipping options
      texture.wrapS = THREE.RepeatWrapping;
      texture.repeat.x = -1;

      // Create a new sphere geometry to hold the panorama image
      const geometry = new THREE.SphereGeometry(500, 60, 40);

      // Flip the geometry inside out so that the image is displayed on the inside of the sphere
      geometry.scale(-1, 1, 1);

      // Create a new material with the loaded texture
      const material = new THREE.MeshBasicMaterial({
        map: texture,
      });

      // Create a new mesh with the geometry and material
      const mesh = new THREE.Mesh(geometry, material);

      // Add the mesh to the scene
      this.scene.add(mesh);

      // Create a new WebGL renderer object
      this.renderer = new THREE.WebGLRenderer();

      // Set the renderer size to the window size
      this.renderer.setSize(window.innerWidth, window.innerHeight);

      // Append the renderer to the document body
      document
        .getElementById("panorama-container")
        .appendChild(this.renderer.domElement);

      // Create a new OrbitControls object to enable mouse drag controls
      this.controls = new THREE.OrbitControls(
        this.camera,
        this.renderer.domElement
      );

      // Disable vertical movement of the camera
      this.controls.enableZoom = false;
      this.controls.enablePan = false;

      // Set the controls to rotate around the panorama image
      this.controls.rotateSpeed = -0.25;

      // Set the render loop
      this.renderer.setAnimationLoop(() => {
        // Update the OrbitControls
        this.controls.update();

        // Render the scene with the camera and renderer
        this.renderer.render(this.scene, this.camera);
      });

      // Resize the renderer when the window size changes
      window.addEventListener("resize", () => {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
      });
    },
  },
};
</script>

<style scoped>
#panorama-container {
  width: 100%;
margin: auto;
}
</style>
