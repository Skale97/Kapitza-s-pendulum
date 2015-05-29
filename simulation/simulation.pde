String lines[] = loadStrings("data.txt");
float[] fip = new float[lines.length];
int i = 0;

void setup() {
  size(640, 480);
  for (int i = 0; i < lines.length; i++) {
    fip[i] = float(lines[i]);
  }
  frameRate(25);
  ellipseMode(CENTER);
}

void draw() {
  i+=50;
  if (i>fip.length-1) i = 0;
  background(255);
  line(320, 250, 320+320*sin(fip[i]), 250+200*cos(fip[i]));
  ellipse( 320+320*sin(fip[i]), 250+200*cos(fip[i]), 10, 10);
  println(fip[i]);
}

