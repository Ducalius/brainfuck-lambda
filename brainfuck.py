
# Usage: brainfuck( code, input )

      
brainfuck =   lambda cd,ip='':(
            lambda c,i,m,p,o,u,st
         ,d,s,t:(lambda oc:[[(lambda
        it:[(lambda ind:[d[ind].append
      (d[ind].pop()+1)])(0 if it == '['
     else (1 if it == ']' else 2)),0 ])(
    chrco ) for           chrco in c] ,t(
   "syntax "+                "err")if d[0]
  [0]> d [                      1][0]else(t
  ("syn"                          +"tax err"
 )if d                             [0][0] < d
 [1][                               0]else 0),[
 None                                for _ in (
 None                                 for (_) in 
                                       iter(lambda
                                        : [ oc[c[o
                                        [0]]]()if c
                                         [o[0] ] in 
                                          oc else 0,
                                          o.append(o
                                           .pop() + 1
                                           ), o[0]][-1
                                           ],len(c)))]
                                         ,''.join(u) ][
                                        -1])( { ('+'):(
                                       lambda : m[p[0] ]
                                      .append( ((m[p[0]])
                                     .pop() + 1) % 256 )),
                                    '-': (lambda : m[p[0] ]
                                   .append((m[p[0]].pop() -1 
                                 )%256 )),('>'): (lambda : p   
                                .append((p.pop() + 1 ) % len(
                               m))),'<': (lambda : p.append((
                              p.pop() - 1 ) %len(m)  )),'.':(
                             lambda:u.append(chr(m    [p[0]][0
                           ]))), ',': (lambda :m[      p[(0)]]
                          .append([m[p[0]].pop()       , ord(i.
                         pop())][1] if len(i)!=         0 else 0
                        )),'[':(lambda:(lambda          oc, c_c:
                       [None for (_) in (None            for _ in
                      iter(lambda: [o.append             (o.pop()
                    + 1), oc.append(oc.pop(               )+ 1) if
                   c[ o[0] ] == '[' else (                [ (c_c).
                  append(c_c.pop() + 1),                   2 if c_c
                 [0] != oc[0] else  0][                     -1  ] if
                c[o[0] ] == ']' else 0                      )  ][-1]
               , 2))] if m[ p[0] ][0]                        ==0 else
             st.append(o[0]))([0],[0                         ]) ),']':
            (lambda : [ o.pop() ,o.                           append (
           st.pop()),st.append(o[0                            ])] if m[ 
          p[0]][0] != 0 else (st.                              pop( ) if
         m[p[0]][0] == 0 else 0)                               )}) ) (cd,
        list(ip), [[(0)] for x                                  in range(
      256)], [0] , [0] , [],[                                   ], [[0],[
     0], [0]],__import__("s"                                    +"y"+ "s", 
    globals() , locals() ,                                       [], (0)),
   (lambda err : (_ for _                                         in () ) .
   throw ( RuntimeError(                                          err) ) ))

 # Hello World to test
print(brainfuck('''++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++
 .>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.
 ------.--------.>+.>.'''))