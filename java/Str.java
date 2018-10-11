import java.util.*;

public class Str {
	public static void main(String[] args) {
		checkString();
		checkList();
		checkLinkedList();
		checkArray();
		checkMap();
		checkSet();
		checkPriorityQueue();
		checkStack();
		checkQueue();
	}

	public static void checkString() {
		String s1 = "abcdefgab";

		assert s1.length() == 9;

		assert s1.substring(1,5).equals("bcde");
		assert s1.substring(2).equals("cdefgab");

		assert s1.indexOf("d") == 3;
		assert s1.indexOf("z") == -1;
		assert s1.indexOf("ab",2) == 7;

		assert s1.replace("abcde", "").equals("fgab");
		assert s1.replaceAll("a", "_").equals("_bcdefg_b");

		String[] lst = s1.split("a");
		String newStr = String.join("_", lst);
		assert newStr.equals("_bcdefg_b");

		StringBuilder s2 = new StringBuilder(s1);
		s2.append("jaja");
		String s2New = s2.toString();
	}

	public static void checkLinkedList() {
		LinkedList<Integer> lst = new LinkedList<>();
		lst.addFirst(1);
		lst.addLast(3);
		lst.add(2,1);
		assert lst.contains(3) == true;
		assert lst.getFirst() == 1;
		assert lst.get(2) == 3;
		
		assert lst.size() == 3;
		for (int i :lst) {
			assert lst.indexOf(i) == i-1;
		}
		lst.remove(2);          // remove index
		lst.removeFirst();
		lst.removeLast();

		assert lst.isEmpty() == true;

	}

	public static void checkList() {
		List<String> lst = new ArrayList<>();
		lst.add("a");
		lst.add("b");
		String[] array = {"c", "d", "e"};

		// need to use object type to transfer to list
		lst.addAll(Arrays.asList(array));

		lst.remove(0);
		lst.remove("b");

		assert lst.size() == 3;
		assert lst.contains("e");
		assert lst.indexOf("e") == 2;

		assert lst.isEmpty();
		lst.clear();
	}

	public static void checkArray() {
		String[][] names = {
            {"Mr. ", "Mrs. ", "Ms. "},
            {"Smith", "Jones"}
        };
        assert (names[0][0] + names[1][0]).equals("Mr. Smith");
        assert names.length == 2;

        // copyOf
        // copyRange
        // sort
	}

	public static void checkMap() {
		// containsKey
		// containsValue
		// get()
		// getOrDefault
		// keySet()
		// put()
		// remove()
		// replace()
	}

	public static void checkSet() {
		// add
		// contains
		// remove
		// isEmpty
		// size
	}

	public static void checkQueue() {
		// add
		// peek
		// remove
	}

	public static void checkStack() {
		// empty
		// peek
		// pop
		// push

	}

	public static void checkPriorityQueue(){
		add
		poll
		peek
		comparator
		PriorityQueue<Node> pq = new PriorityQueue<>(new aComparator());

		class aComparator implements Comparator<Node> {
			public int compare(Node n1, Node n2) {
				if (n1.val < n2.val) {
					return 1;
				} else if (n1.val > n2.val) {
					return -1;
				} else {
					return 0;
				}

			}
		}
	}
}