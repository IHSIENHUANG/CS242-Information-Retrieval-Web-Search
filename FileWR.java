import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
public class FileWR {
	static FileWriter writer;
	public FileWR(String fileName){
		try {
			writer = new FileWriter(fileName+".csv",true);
		} catch (IOException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}
	}
 
	public static void writeFile(String text) throws IOException {
		writer.write(text);
	}
 
	public static void close(){
		try {
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
