Finding the Efficiency of the Xylem and Money Maker Treadle Pumps
=================================================================


Introduction
------------
Small scale farmers use human-powered water pumps in rural areas to increase crop yields beyond subsistence levels. Different designs utilize various biomechanical motions. One of the most popular and proven designs for human-powered water pumps is the treadle pump, which is operated via a stepping motion (Figure 1).


.. image:: https://lh3.googleusercontent.com/hT66A6hgEXVfN3xNONnjnuBixqWGehWg-135Xf51JqBMLFJB_CrvkwrsgDLRPAZW12z3hfkJipN2U8msN-6JAlmLqXaapxFY2IDHZTJ6
   :width: 50%
   :align: center
   :alt: Treadle Example.


*Figure 1. A user “treadles” on the Money Maker treadle pump.*


The treadle pump is an inexpensive and portable irrigation tool. According to International Development Enterprises (IDE), treadle pumps helped farmers in Bangladesh increase their income by an average of $100 a year. This increase in profit allowed farmers to invest in larger, more expensive irrigation machines that further increased crop yields and helped create financial stability [Polak]_.
        
A prototype pedal-powered centrifugal water pump was tested by Abe McKay during his Master’s studies [McKay]_. Mckay’s tests suggested that this pump’s efficiency was comparable to that of the commercially available Xylem and Money Maker treadle pumps. Detailed efficiency data for these treadle pumps are not available and thus an accurate comparison could not be made until now.


For our experiment, we gathered efficiency data from the Xylem and Money Maker treadle pumps and compared them to McKay’s data on the prototype Buffalo pump. By comparing the efficiency of the Buffalo pump to the commercially available Xylem and Money Maker pumps, we can evaluate the prototype’s potential for success as a low cost tool for small scale irrigation.


Methods
-------
McKay had conducted an efficiency test with the centrifugal pump so our goal was to conduct a similar test with our treadle pumps in order to produce data that could be compared. We conducted fifteen tests, with three replicates at each pressure head between 1 and 5 meters. We pumped 20 liters of water for each test. We measured time using a photoresistor that was covered and uncovered (on/off) to record the beginning and end of each test. The DAQ apparatus including photoresistor circuit, sensor wires, and LabJack is shown in Figure 2 below.


.. image:: https://lh4.googleusercontent.com/dNVPUmycRO_iXPjoPFALiH6WhI5BUFCNH_PAPEzaWKpgmdw-b_2nfR_jFlQS_V5Rgi9CO9BX-bsQNuVaBeddpYjwIlM6_zJwk-0p1PBv
   :width: 50%
   :align: center
   :alt: DAQ Setup.


*Figure 2. The LabJack was kept dry and out of danger behind the treadle pump.*


Force sensors were designed using steel plates and two 200 kg rated load cells. The load cells were mounted between steel plates and then mounted on the treadle pump lever arms with U-bolts. We calibrated the force sensor using Olympic weights and a balance scale for reference. The power meter apparatus consisting of the force sensors and angular rate gyro are shown below in Figure 3. 


.. image:: https://lh4.googleusercontent.com/Cj0WrONEkAyHNwwyYlWDzWVg_sNJjJRDVVkPfnxdajdjAroGYe8wZyEDp5xF8pTE-32bxs1B91me7J7TKFcNwfvaPBUBQKMTWMDLq2Tg
   :width: 50%
   :align: center
   :alt: Treadle Pump Setup.
        
*Figure 3. The Xylem treadle pump with force sensor and angular rate gyro attached*


We measure force and angular rate using the force sensors and the angular rate gyro respectively. Using our force measurements, we were able to calculate torque using the equation below\: 


.. image:: https://lh3.googleusercontent.com/n_7qmoLk7L4qJZq67t2d_qu1ehF8E5rj830WKLmCjzX_-5cuelLyDnC3PAm9J2WxHLH0ssLmUoGK8wpRScsI32ODADaKwWxT6pNaQH4
   :align: center
   :alt: Torque Equation.


where *F* is the force in Newtons applied to the lever arm perpendicular to the arm. The radius *r* is the distance from the point of applied force to the lever arm’s center of rotation. Using torque and angular rate measurements from the angular rate gyro, power in watts is calculated using the equation below:


.. image:: https://lh4.googleusercontent.com/Yg6OEnpXQgHgKvAHfg7cZYcbwLPsugQJLAeEUdKTs8a4V4ns5NQByj3dddBMbwBdbA9eKcMynU4bBzmCXXEHYu2DX6Kb8zCWUOb1UbE
   :align: center
   :alt: Power Equation.


where torque |tau| is in Newton-meters and angular velocity |omega| is in radians per second. Time required to fill the 20 liter bucket was measured and used to calculate flow rate. Hydraulic power could then be calculated using the equation:


.. |tau| image:: https://lh4.googleusercontent.com/KX7lusK2lC6kkoMuemkSLkz3Kw4gKJ1QSVEBdq0YVP5BytYucw0WFU_wqRoMndEYJDioqlrsRRclHf-_aw06-2klbqtdVbFDxzVCoQ4
   :width: 15
   :alt: Tau.


.. |omega| image:: https://lh4.googleusercontent.com/rrqhKha867UYLs8imApM79QDYnda6dkYl0O_DqezrWSKGPIOo36c36yEIPNmZ7c2kVv9hvMDecWY1ONrs4HSJSyXeNVwjUfjinnKfIc
   :width: 15
   :alt: Sigma.


.. image:: https://lh6.googleusercontent.com/lMaqYEDMnRPV6Up0yhtiDaCL4r_Zlw3ShfQanOh-vufaXi2wXvfgikk0tDvV9ekhilGFBAYoXAvHYNG3VApkuXp7dljVFlxSdk_epD8
   :align: center
   :alt: Hydraulic Power.


Simplifying for water, where density equals 1 kilogram per liter\:


.. image:: https://lh4.googleusercontent.com/-_0e_P48SrcRLVNJkf27Bq4b1DN2sdLMyTKn5Ka-Lura9_sUmh5ZxdDqkniyIGJe-3M6_wealPhF047KYadWdg08DUkaL95GX1AOrm0
   :align: center
   :alt: Simplified Hyrdualic Power.


where *q* is measured in liters per second, *g* is 9.81 meters per second squared, and *h* is vertical pressure head measured in meters. Efficiency can be calculated using the equation below:


.. image:: https://lh4.googleusercontent.com/0uDZGmKRtCq7kD5hsu6xCUqG0WQjX-WTvGU0Ne6XrtQgdpZB04ofB5MG_tm2ykD8BWkuSCUfAKgpYmzuce1CpygprGJo0E_exEFUnVI
   :align: center
   :alt: Power Efficiency.


Hazen efficiency is determined by calculating the friction head loss using the Hazen-Williams equation:


.. image:: https://lh4.googleusercontent.com/pCp5rweFd8w0qTPNGqN2uwGIubHKb0I_2A00-x0C2lZfmI6erYfFg0TtVGdE5WRVp2CR2AMcAx8leAUnU7LdeUIdBLzC8Fe6AjCUc5njOJoq9EBuX_gVFjZW2y0OvPxt-s93xsJj
   :align: center
   :alt: Hazen-Williams Head Loss Equation.


Hydraulic power is adjusted using this estimated friction head. A Hazen efficiency can then determined.


Each test began with one person priming the pump in order to achieve consistent water flow. The collector would deliver the pumped water into an overflow bucket until the experiment began. At the start of the experiment the treadler would remove a piece of paper covering the photoresistor. Simultaneously, the collector would transfer the outlet hose to the 20 L metered collection bucket. During the data collection, the treadler would attempt to maintain an average of 100 Watts. This was done by feel only and therefore resulted in some deviation from the target power. The experiment ended when the collector signaled to the treadler that 20 L was reached, at which point the photoresistor was covered and the data collection complete. The data was collected via a MATLAB program and saved after each trial. 15 trials were completed: three at each meter interval between 1 and 5 meters.


Results
-------


.. image:: https://lh6.googleusercontent.com/c1m-hjz1AZFLr6aSqJGY_K_mZ5RJE1mUVRr88hBpd7Myf0mD8qdLpsL_z1hkqanhy7YnXg1mrB0c5-8NdhdkIc7HcuE_ERNuOwMeye-8
   :align: center
   :alt: 1m Trials.
     
*Figure 4*


.. image:: https://lh4.googleusercontent.com/GwFm7DxkDij0VktJ5IbzfLfgIoPLMTbMBF9lUEWVT2DiN8D-U3LcimtZrTCR1VRXexCY0bhG5rU2jT4xByTFP-fcM_PdHcYyR3ILr9s4
   :align: center
   :alt: 2m Trials.


*Figure 5*


.. image:: https://lh4.googleusercontent.com/RB2nmNmj2FR0n9KjxxBrXXRT1KffBg7asDdBdj2bgq56GaE6HU1Dyf8xkei0gqDhJrcnes6G4BqAwTRE07xBDVqr43iwXsDkjm4BtiIL
   :align: center
   :alt: 3m Trials.


*Figure 6*




.. image:: https://lh3.googleusercontent.com/j_0u2RYK_dvJFm5B55Evy2omZIPQ3OyEIECPfixTx3n28WTD1-5CPNPo8G0SSMlAswqZNzbczAvorGP1UJyICtYXjwku4U4CSuzlELVW
   :align: center
   :alt: 4m Trials.


*Figure 7*


.. image:: https://lh5.googleusercontent.com/qDc5i-EADguQQfqlZCun2r-K19QyMgFFWG2fkqcurfswlOXNemo86_YXM6HjjSZcz9stY9QKFx19vgWTUAyEOh3Lh39fIIcrbE7Zgj68
   :align: center
   :alt: 5m Trials.


*Figure 8*


The figures 4-8 above show the calculated efficiencies for each pump at different pressure heads across all trials. The average efficiencies are graphed in figure 9 below.


.. image:: https://lh6.googleusercontent.com/Q1lsaZbAJQNeCTgGN3fCubrsy-shyZvudng5Mb9kCS3YRYhPt-lvsBbc0IkdKk_juLk8acZoyftBYWggLfaAqR8S_3LouzYDeF7BkFA_
   :align: center
   :alt: Average Efficiency.


Figure 9 shows the efficiency trends across different pressure heads for each pump. The average efficiency was found by finding the mean across the three trial tests at each pressure head. The effect that the variation in power may have had on efficiency was assumed to be negligible. The trendlines and corresponding equations are shown.


Discussion
----------


There is a variation in average power within each testing group that must be acknowledged. Because the average power for each testing group was not held constant, we must consider the relationship between power and efficiency. When the trendlines for each testing group are observed, our data does not suggest a strong relationship between average power and efficiency within a given pressure head. More data points and a dedicated testing procedure would help validate this claim, but the observed results are enough to make the assumption that the effect of any hypothetical correlation is negligible given the range over which average power varied during our tests. Therefore, the average efficiencies can be compared between pumps where pressure head is held constant despite fluctuating average power measurements across trials.  


Figure 9 shows the average efficiencies for each pump at various pressure heads. The centrifugal Buffalo pump has a negatively sloped trendline whereas the treadle pumps have positively sloped trendlines when observed between our range of pressure heads. The Xylem pump surpasses the efficiency of the Buffalo pump around 4.5 meters pressure head. The Money Maker pump can be predicted to surpass the efficiency of the Buffalo pump at around 5.5 meters pressure head. The Xylem and Money Maker pumps share a similar relationship between increased pressure head and increased efficiency. There is a difference in slope between the two trendlines of 0.54. Due to shared mechanical properties, all treadle-type pumps most likely produce similarly sloped trendlines. The centrifugal Buffalo pump is a completely different design, and thus its efficiency can be predicted along a completely different trendline.
        
The Buffalo pump is determined to be 21% (|sigma| = 6.7%) more efficient at 1 meter pressure head than the Xylem pump, and 32% (|sigma| = 4.9%) more efficient at the same head when compared to the Money Maker. At 2 meters pressure head, the Buffalo pump was 17.0% (|sigma| = 2.9%) and 24.7% (|sigma| = 2.4%) more efficient than the Xylem and Money Maker respectively. At 3 meters head, it was 16.3% (|sigma| = 3.8%) and 26% (|sigma| = 4.1%) more efficient respectively. At 4 meters, the differences decreased to 2.2% (|sigma| = 4.6%) and 9.7% (|sigma| = 4.6%). At 5 meters the Xylem pump was 6.8% (|sigma| = 4.9%) more efficient than the Buffalo pump and the Money Maker was only 2% (|sigma| = 3.7%) less efficient than the Buffalo. 


.. |sigma| image:: https://lh5.googleusercontent.com/-G903hViWdwTXxIBdQ-Uo0ClETR6zsbyontd4T4wXBeNEXC19kJ0sF6KVQvD7VKDnMuI89JFBvE-H4BGXkaCPrvXMNh_TajS6blxF7zEvcMG5rvclqnbTciQDokNLDjx1sW5EsTY
   :width: 15
   :alt: Sigma.


Until the correlation between power and efficiency can be determined, these conclusions include an error assumed to be negligible. It is within the best interest of further research to try and describe this correlation, which may appear something like this:


.. image:: https://lh5.googleusercontent.com/oSzmb9K3s_EEldU7vt7d5QzDEWlAG8eiX7fP0Q8BU2C-rURN0SR2KHf7ARsQYtX6bYGSFZz2l3MOoBccZgBc4t98EdyWjckxA6PpoYis_Z19NJxC0x7S1ncWH8sVLqeIaLE4e-6x
   :align: center
   :alt: Power Efficiency Correlation.
        
For low C values (<<1), our assumption can be considered valid. Our current assumption is that C=0, where efficiency is not a function of power. It would also be beneficial to direct further research at determining the range of pressure heads most frequently encountered in real world irrigation situations. This information will be critical in determining which human powered water pump is the most efficient for its given application.


Conclusion
----------


Our research finds that the Buffalo pump is more efficient than the Xylem treadle pump up to 4.5 meters pressure head, and the Money Maker up to 5.5 meters pressure head. The efficiency advantage of one type of pump over another will depend largely on pressure head. Figure 9 shows the efficiency trends between two treadle style pumps and a centrifugal-type water pump.  






**References**


.. [Polak]        P. Polak, “How IDE Installed 1.5 Million Treadle Pumps in Bangladesh by Activating the Private Secotr: The Practical Steps,” International Development Enterprises (IDE), 2000.


.. [McKay]        A. Mckay. (2018), “The Water Buffalo: Design of a Portable Bicycle Powered Irrigation Pump for Small-Scale African Farmers” UC Davis, Davis, California