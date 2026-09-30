# SmartCare Human vs AI Comparison

| Question | Human Version | AI Version |
|---|---|---|
| Easy to understand? | Yes. The code is simple and uses basic Python concepts. | Yes. The suggested use of lists and dictionaries was easy to understand. |
| Runs successfully? | Yes. The program runs and displays appointments. | Yes. The suggested approach works with the prototype. |
| Uses only required features? | Yes. It focuses on storing and displaying appointments. | Yes. The suggestion stayed within lists, dictionaries and functions. |
| Adds assumptions? | Very few assumptions are made. | The AI assumed that a list of dictionaries was a suitable way to organise the appointment data. |
| Handles errors? | Partly. It rejects an empty patient name and an empty appointment time, but it does not prevent double-booking. | The AI approach helped organise the data but still requires testing and validation by the developer. |
| Could I explain it? | Yes. I understand how the appointments are stored and displayed. | Yes. I can explain why lists and dictionaries are being used. |

## Conclusion

Both approaches are suitable for a beginner SmartCare prototype. AI was useful for suggesting how the appointment data could be organised, but I still needed to understand, run and test the code myself. Testing also showed that the current prototype allows two patients to be booked with the same practitioner at the same time, so further improvement is needed.