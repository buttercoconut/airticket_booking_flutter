class Flight {
  final String flightNumber;
  final String airline;
  final String origin;
  final String destination;
  final double price;

  Flight({
    required this.flightNumber,
    required this.airline,
    required this.origin,
    required this.destination,
    required this.price,
  });

  factory Flight.fromJson(Map<String, dynamic> json) {
    return Flight(
      flightNumber: json['flightNumber'] as String,
      airline: json['airline'] as String,
      origin: json['origin'] as String,
      destination: json['destination'] as String,
      price: (json['price'] as num).toDouble(),
    );
  }
}
