class Flight {
  final String airline;
  final String flightNumber;
  final String departureCity;
  final String arrivalCity;
  final String departureTime;
  final String arrivalTime;
  final double price;

  Flight({
    required this.airline,
    required this.flightNumber,
    required this.departureCity,
    required this.arrivalCity,
    required this.departureTime,
    required this.arrivalTime,
    required this.price,
  });
}
