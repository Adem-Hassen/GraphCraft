import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64


def function_graph(ch):
  
    x = np.linspace(-10, 10, 1000)
    if ch=='sin(x)':
      sin=np.sin(x)
      plt.figure(figsize=(12,8))
      plt.plot(x, sin, label='Function: y = sin(x)')

    
      plt.grid(True)
      plt.xlim(-10,max(x))
    
      plt.axhline(0, color='black',linewidth=0.5)
      plt.axvline(0, color='black',linewidth=0.5)

    
      plt.xlabel('X-axis')
      plt.ylabel('Y-axis')
      plt.title('Direct Orthonormal Coordinate System')
      plt.legend()


      
      buffer = BytesIO()
      plt.savefig(buffer, format='png')
      buffer.seek(0)
      plt.close()

      
      image_png = buffer.getvalue()
      buffer.close()
      graphic = base64.b64encode(image_png).decode('utf-8')
      return graphic
    elif ch=='cos(x)':
        cos=np.cos(x)
        plt.figure(figsize=(12,8))
        plt.plot(x, cos, label='Function: y = cos(x)')

      
        plt.grid(True)
        plt.xlim(-10,max(x))
      
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)

      
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Direct Orthonormal Coordinate System')
        plt.legend()

        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png).decode('utf-8')
        return graphic
    elif ch=='log(x)':
        x = np.linspace(-10, 25, 1500)
        log=np.log10(x)
        plt.figure(figsize=(12,8))
        plt.plot(x, log, label='Function: y = log(x)')

      
        plt.grid(True)
        plt.xlim(-10,max(x))
      
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)

      
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Direct Orthonormal Coordinate System')
        plt.legend()

        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png).decode('utf-8')
        return graphic
    elif ch=='ln(x)':
        x = np.linspace(-10, 25, 1500)
        ln=np.log(x)
        plt.figure(figsize=(12,8))
        plt.plot(x, ln, label='Function: y = ln(x)')

      
        plt.grid(True)
        plt.xlim(-10,max(x))
      
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)

      
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Direct Orthonormal Coordinate System')
        plt.legend()

        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png).decode('utf-8')
        return graphic
    elif ch=='exp(x)':
        x = np.linspace(-3, 5, 1000)
        exp=np.exp(x)
        plt.figure(figsize=(12,8))
        plt.plot(x, exp, label='Function: y = exp(x)')

      
        plt.grid(True)
        plt.xlim(-3,max(x))
      
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)

      
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Direct Orthonormal Coordinate System')
        plt.legend()

        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png).decode('utf-8')
        return graphic
    elif ch=='tan(x)':
        x = np.linspace(-1.4, 1.4, 1000)
        tan=np.tan(x)
        plt.figure(figsize=(12,8))
        plt.plot(x, tan, label='Function: y = tan(x)')

      
        plt.grid(True)
        plt.xlim(-1.4,max(x))
      
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)

      
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Direct Orthonormal Coordinate System')
        plt.legend()

        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png).decode('utf-8')
        return graphic
    elif ch=='sqrt(x)':
        x = np.linspace(-2, 2, 2000)
        sqrt=np.sqrt(x)
        plt.figure(figsize=(12,8))
        plt.plot(x, sqrt, label='Function: y = sqrt(x)')
        
      
        plt.grid(True)
        plt.xlim(-2,max(x))
        plt.ylim(-2,max(x))
      
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)

      
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Direct Orthonormal Coordinate System')
        plt.legend()

        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png).decode('utf-8')
        return graphic
    
       
    else:
       
       
       return False

