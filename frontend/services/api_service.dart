import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/flight.dart';

class ApiService {
  static const String _baseUrl = 'https://api.example.com';

  Future<List<Flight>> searchFlights({
    required String departureCity,
    required String arrivalCity,
    required String date,
  }) async {
    final uri = Uri.parse('$_baseUrl/flights/search').replace(queryParameters: {
      'departure': departureCity,
      'arrival': arrivalCity,
      'date': date,
    });

    final response = await http.get(uri);
    if (response.statusCode != 200) {
      throw Exception('Failed to load flights');
    }

    final List<dynamic> data = jsonDecode(response.body);
    return data.map((json) => Flight(
          airline: json['airline'],
          flightNumber: json['flightNumber'],
          departureCity: json['departureCity'],
          arrivalCity: json['arrivalCity'],
          departureTime: json['departureTime'],
          arrivalTime: json['arrivalTime'],
          price: (json['price'] as num).toDouble(),
        )).toList();
  }
}
