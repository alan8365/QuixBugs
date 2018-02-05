package java_testcases.junit;

import static org.junit.Assert.*;
import org.junit.Test;
import java_programs.TO_BASE;
import com.google.gson.JsonParser;

public class TO_BASE_TEST {
  /**
   * Junit test case for TO_BASE generated by tests generator.
   */
  @Test(timeout = 100)
  public void to_base_test1() {
    try {
      Object actual = TO_BASE.to_base((int)31,(int)16);
      assertEquals("\"1F\"",actual.toString() );
    }
    catch(IllegalArgumentException e) {
      throw new IllegalArgumentException("Arguments are illegal!") ;
    }
  }

  @Test(timeout = 100)
  public void to_base_test2() {
    try {
      Object actual = TO_BASE.to_base((int)41,(int)2);
      assertEquals("\"101001\"",actual.toString() );
    }
    catch(IllegalArgumentException e) {
      throw new IllegalArgumentException("Arguments are illegal!") ;
    }
  }

  @Test(timeout = 100)
  public void to_base_test3() {
    try {
      Object actual = TO_BASE.to_base((int)44,(int)5);
      assertEquals("\"134\"",actual.toString() );
    }
    catch(IllegalArgumentException e) {
      throw new IllegalArgumentException("Arguments are illegal!") ;
    }
  }

  @Test(timeout = 100)
  public void to_base_test4() {
    try {
      Object actual = TO_BASE.to_base((int)27,(int)23);
      assertEquals("\"14\"",actual.toString() );
    }
    catch(IllegalArgumentException e) {
      throw new IllegalArgumentException("Arguments are illegal!") ;
    }
  }

  @Test(timeout = 100)
  public void to_base_test5() {
    try {
      Object actual = TO_BASE.to_base((int)56,(int)23);
      assertEquals("\"2A\"",actual.toString() );
    }
    catch(IllegalArgumentException e) {
      throw new IllegalArgumentException("Arguments are illegal!") ;
    }
  }

  @Test(timeout = 100)
  public void to_base_test6() {
    try {
      Object actual = TO_BASE.to_base((int)8237,(int)24);
      assertEquals("\"E75\"",actual.toString() );
    }
    catch(IllegalArgumentException e) {
      throw new IllegalArgumentException("Arguments are illegal!") ;
    }
  }

  @Test(timeout = 100)
  public void to_base_test7() {
    try {
      Object actual = TO_BASE.to_base((int)8237,(int)34);
      assertEquals("\"749\"",actual.toString() );
    }
    catch(IllegalArgumentException e) {
      throw new IllegalArgumentException("Arguments are illegal!") ;
    }
  }

}