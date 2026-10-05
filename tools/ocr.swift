import Foundation
import AppKit
import PDFKit
import Vision

func recognize(_ image: CGImage) throws -> String {
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = false
    try VNImageRequestHandler(cgImage: image).perform([request])
    return (request.results ?? []).compactMap { $0.topCandidates(1).first?.string }.joined(separator: "\n")
}
let input = CommandLine.arguments[1]
let output = CommandLine.arguments[2]
var sections: [String] = []
if input.lowercased().hasSuffix(".pdf") {
    guard let document = PDFDocument(url: URL(fileURLWithPath: input)) else { fatalError("Cannot open PDF") }
    for index in 0..<document.pageCount {
        try autoreleasepool {
            let page = document.page(at: index)!
            let bounds = page.bounds(for: .mediaBox)
            let image = page.thumbnail(of: NSSize(width: bounds.width * 2.5, height: bounds.height * 2.5), for: .mediaBox)
            var rect = CGRect(origin: .zero, size: image.size)
            guard let cg = image.cgImage(forProposedRect: &rect, context: nil, hints: nil) else { fatalError("Cannot render") }
            sections.append("## Page \(index + 1)\n\n" + (try recognize(cg)))
        }
        print("Page \(index + 1)/\(document.pageCount)")
    }
} else {
    guard let image = NSImage(contentsOfFile: input) else { fatalError("Cannot open image") }
    var rect = CGRect(origin: .zero, size: image.size)
    guard let cg = image.cgImage(forProposedRect: &rect, context: nil, hints: nil) else { fatalError("Cannot render") }
    sections.append(try recognize(cg))
}
try sections.joined(separator: "\n\n").write(toFile: output, atomically: true, encoding: .utf8)
