import requests
from bs4 import BeautifulSoup

print(""" 

*******   *******   ********  ******  **   ** ** ***************** *******  
/**////** /**////** /**/////  **////**/**  ** /**/////**///**///// /**////** 
/**    /**/**   /** /**      **    // /** **  /**    /**  /**      /**   /** 
/**    /**/*******  /*******/**       /****   /**    /**  /******* /*******  
/**    /**/**///**  /**//// /**       /**/**  /**    /**  /**////  /**///**  
/**    ** /**  //** /**     //**    **/**//** /**    /**  /**      /**  //** 
/*******  /**   //**/********//****** /** //**/**    /**  /********/**   //**
///////   //     // ////////  //////  //   // //     //   //////// //     // 
    
    Made by jagstang67 with proud .................
    
""")

print(" Program ini berfungsi merubah scan QR code menjadi XML file")

# Prompt the user for a list of URL/filename pairs
url_filenames = []
while True:
    url = input("Scan QR Label Faktur nya (Enter kalo sudah selesai ! ): ")
    if not url:
        break
    filename = input("Tentukan Nama File agar di save jadi XML Document: ")
    url_filenames.append((url, filename))


for url, filename in url_filenames:

    response = requests.get(url)

    
    soup = BeautifulSoup(response.content, "xml")

    
    with open(filename, "w") as file:
        file.write(str(soup))

    print(f"Document XML {url} tersimpan sebagai {filename}")