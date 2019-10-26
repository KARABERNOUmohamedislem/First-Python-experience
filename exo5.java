import java.util.Scanner;
class Point {
private int x;
private int y;
public Point(int absc, int ord){
x = absc;
y = ord;
}
public void deplacer (int dx, int dy){
x = x + dx;
y = y + dy;}
public void afficher(){
System.out.println("Mes coordonnées sont x = "+x+" et y ="+y);}}

class testpoint {
public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir x :");
        int x = sc.nextInt();
        System.out.println("Veuillez saisir y :");
        int y = sc.nextInt();
        Point p = new Point(x, y);   
    p.afficher();
    
}
}