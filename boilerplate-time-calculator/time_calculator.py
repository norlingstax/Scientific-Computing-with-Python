def add_time(start, duration):
  pieces=start.split()
  time=pieces[0]
  ampm=pieces[1]
  shours=time.split(':')[0]
  sminutes=time.split(':')[1]
  shours=int(shours)
  sminutes=int(sminutes)
  
  dhours=duration.split(':')[0]
  dminutes=duration.split(':')[1]
  dhours=int(dhours)
  dminutes=int(dminutes)
  
  new_h=shours+dhours
  new_m=sminutes+dminutes
  #print('before ',new_h,new_m)
  
  if new_m>59:
      new_m-=60
      new_h+=1
  
  if new_m < 10:
      new_m='0'+str(new_m)
  
  check=new_h//12 
  if check%2==0:
      if ampm=='AM':
          ampm='AM'
      else: ampm='PM'
  else:
      if ampm=='AM':
          ampm='PM'
      else: 
          ampm='AM'
          new_h+=12
      
      
  #print('after ',new_h,new_m)  
  if new_h>12 and new_h<24:
      new_h-=12
      #print('inside ',new_h,new_m)
      new_time=str(new_h)+':'+str(new_m)+' '+ampm
  elif new_h>=24 and new_h<36:
      new_h-=24
      #print('inside ',new_h,new_m)
      new_time=str(new_h)+':'+str(new_m)+' '+ampm+' (next day)'
  elif new_h>=36:
      d=new_h//24
      new_h-=24*d
      if new_h==0:
          new_h=12
      #print('inside ',new_h,new_m)
      new_time=str(new_h)+':'+str(new_m)+' '+ampm+' ('+str(d)+' days later)'
  elif new_h<=12:
      new_time=str(new_h)+':'+str(new_m)+' '+ampm
  
  return new_time
