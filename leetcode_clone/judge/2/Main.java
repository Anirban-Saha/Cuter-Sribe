import java.util.*;

public class Main{
	public static void main(String [] args){
		Scanner sc = new Scanner(System.in);
		Main main = new Main();
		int T = sc.nextInt();
		while (T-- > 0){
			int n = sc.nextInt();
			int [] nums = new int[n];
			for(int i = 0; i<n; i+=1){
				nums[i] = sc.nextInt();
			}
			int target = sc.nextInt();
			boolean result = main.linearSearch(nums, target);
			System.out.println(result);
		}
	}
	public boolean linearSearch(int [] nums, int target){
		for(int i : nums){
			if(i == target)
				return true;
		}
		return false;
	}
}
