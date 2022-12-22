import java.rmi.Remote;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DaytimeImpl extends UnicastRemoteObject implements Daytime {
	public DaytimeImpl() throws RemoteException {
	}
	
	public String getTime() {
		return java.time.Clock.systemUTC().instant().toString();
	}
}
