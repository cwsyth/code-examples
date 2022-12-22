import java.rmi.Naming;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DaytimeClient {
	public static void main(String args[]) throws Exception {
		String host = args[0];
		
		String local = java.time.Clock.systemUTC().instant().toString();
		System.out.println("Local starttime is	" + local);
		
		Daytime remote = (Daytime) Naming.lookup("//" + host + "/time");
		String received = remote.getTime();
		System.out.println("Received time is	" + received);

		String later = java.time.Clock.systemUTC().instant().toString();
		System.out.println("Local starttime is	" + later);
	}
}
