package java_testcases.junit;

import static org.junit.Assert.*;
import org.junit.Test;
import java_programs.NEXT_PALINDROME;
import com.google.gson.JsonParser;

public class NEXT_PALINDROME_TEST {
  /**
   * Junit test case for NEXT_PALINDROME generated by tests generator.
   */
  @Test(timeout = 100)
  public void next_palindrome_test1() {
    try {
      Object actual = NEXT_PALINDROME.next_palindrome(new int[]{1,4,9,4,1});
      assertEquals("[1,5,0,5,1]",actual.toString() );
    }
    catch(IllegalArgumentException e) {
      throw new IllegalArgumentException("Arguments are illegal!") ;
    }
  }

  @Test(timeout = 100)
  public void next_palindrome_test2() {
    try {
      Object actual = NEXT_PALINDROME.next_palindrome(new int[]{1,3,1});
      assertEquals("[1,4,1]",actual.toString() );
    }
    catch(IllegalArgumentException e) {
      throw new IllegalArgumentException("Arguments are illegal!") ;
    }
  }

  @Test(timeout = 100)
  public void next_palindrome_test3() {
    try {
      Object actual = NEXT_PALINDROME.next_palindrome(new int[]{4,7,2,5,5,2,7,4});
      assertEquals("[4,7,2,6,6,2,7,4]",actual.toString() );
    }
    catch(IllegalArgumentException e) {
      throw new IllegalArgumentException("Arguments are illegal!") ;
    }
  }

  @Test(timeout = 100)
  public void next_palindrome_test4() {
    try {
      Object actual = NEXT_PALINDROME.next_palindrome(new int[]{4,7,2,5,2,7,4});
      assertEquals("[4,7,2,6,2,7,4]",actual.toString() );
    }
    catch(IllegalArgumentException e) {
      throw new IllegalArgumentException("Arguments are illegal!") ;
    }
  }

  @Test(timeout = 100)
  public void next_palindrome_test5() {
    try {
      Object actual = NEXT_PALINDROME.next_palindrome(new int[]{9,9,9});
      assertEquals("[1,0,0,1]",actual.toString() );
    }
    catch(IllegalArgumentException e) {
      throw new IllegalArgumentException("Arguments are illegal!") ;
    }
  }

}